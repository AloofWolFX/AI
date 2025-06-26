import os
from tqdm import tqdm
import torch
from vllm import LLM, SamplingParams
from huggingface_hub import snapshot_download

# Model configuration
model_name = "Satori-reasoning/Satori-7B-Round2"
local_path = os.path.join(os.path.abspath(
    "/"), "model", "HuggingFace")
model_path = os.path.join(local_path, model_name)

# Check if the model has been downloaded, if not download it
if not os.path.exists(model_path):
    print(f"Downloading model {model_name} to {local_path}...")
    snapshot_download(
        repo_id=model_name,
        local_dir=os.path.join(local_path, model_name),
        local_dir_use_symlinks=False
    )
    print("Model download complete!")
else:
    print(f"Model already exists in {local_path}，Skip download")

# Global LLM Instance
llm = LLM(
    model=model_path,
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
    # Add current question
    prompt = f"Please solve the following math problems:\n{question}\n\nPlease use rigorous mathematical reasoning to answer this question and mark the final answer with \\boxed{{}} at the end."
    return prompt
