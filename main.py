import os
from tqdm import tqdm
import torch
from vllm import LLM, SamplingParams

# 全局LLM实例
model_path = "Satori-reasoning/Satori-7B-Round2"
llm = LLM(
    model=model_path,
    trust_remote_code=True,
    tensor_parallel_size=1,
)


def generate(question_list):
    sampling_params = SamplingParams(
        max_tokens=4096,
        temperature=0.0,
        n=1,
        # hide special tokens such as "<|continue|>", "<|reflect|>", and "<|explore|>"
        skip_special_tokens=True
    )
    outputs = llm.generate(question_list, sampling_params, use_tqdm=True)
    completions = [[output.text for output in output_item.outputs]
                   for output_item in outputs]
    return completions


def prepare_prompt(question, history=None):
    # 添加当前问题
    prompt = f"<|im_start|>user\nSolve the following math problem efficiently and clearly.\nPlease reason step by step, and put your final answer within \\boxed{{}}\nProblem: {question}<|im_end|>\n<|im_start|>assistant\n"
    return prompt
