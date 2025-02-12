import os
from tqdm import tqdm
import torch
from vllm import LLM, SamplingParams
from huggingface_hub import snapshot_download

# 模型配置
model_name = "Satori-reasoning/Satori-7B-Round2"
local_path = os.path.join(os.path.abspath(
    "."), "model", "HuggingFace")

# 检查模型是否已下载，如果没有则下载
if not os.path.exists(os.path.join(local_path, model_name)):
    print(f"正在下载模型 {model_name} 到 {local_path}...")
    snapshot_download(
        repo_id=model_name,
        local_dir=os.path.join(local_path, model_name),
        local_dir_use_symlinks=False
    )
    print("模型下载完成！")
else:
    print(f"模型已存在于 {local_path}，跳过下载")

# 全局LLM实例
llm = LLM(
    model=model_name,
    trust_remote_code=True,
    tensor_parallel_size=1,
    download_dir=local_path
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
    prompt = f"请解答以下数学问题：\n{question}\n\n请用严谨的数学推理过程来解答这个问题，并在最后用\\boxed{{}}标注最终答案。"
    return prompt
