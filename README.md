# Satori-7B-Round2-WebUI

`Satori-7B-Round2`  model has only 7B parameters, but its mathematical reasoning ability surpasses 70B and a number of small models. The Satori-7B-Round2 reasoning model trained by MIT and Harvard based on ` Chain of Actions and Thoughts` mechanism. 

This project provides a friendly Web UI based on the Satori-7B-Round2 inference model and Gradio API, which allows you to quickly deploy an instance and immediately experience the inference capabilities of the Satori-7B-Round2 model. 

## What is Satori-7B-Round2

Satori-7B-Round2 is a 7B parameter large language model launched by researchers from **MIT, Harvard University** and other institutions, focusing on improving reasoning capabilities. Based on Qwen-2.5-Math-7B, Satori achieves advanced reasoning performance through small-scale format fine-tuning and large-scale reinforcement learning.


The model introduces the Chain of Actions and Thoughts (COAT) mechanism, which guides the model to reason through special meta-action tags. Satori performs well in mathematical reasoning and cross-domain tasks, showing excellent generalization ability.

### Core features of Satori-7B-Round2

- Autoregressive search capability: Satori can perform autoregressive search by self-reflection and exploring new strategies, completing complex reasoning tasks without external guidance. 
- Mathematical Reasoning: Satori achieved top scores on the mathematical reasoning benchmark test, demonstrating excellent reasoning skills. 
- Cross-domain tasks: In addition to mathematics, Satori also performs well in cross-domain tasks such as logical reasoning, code reasoning, common sense reasoning, and table reasoning, and has strong generalization ability.
- Self-reflection and error correction ability: Satori can self-reflect and self-correct during the reasoning process, which improves the accuracy of reasoning.
- Reinforcement Learning Optimization: It adopts the Chain of Actions and Thoughts (COAT) mechanism and a two-stage training framework, including small-scale format tuning and large-scale self-optimization, and mainly relies on reinforcement learning (RL) to achieve advanced reasoning performance.


### Technical principle of Satori-7B-Round2——COAT

![Satori](https://s2.loli.net/2025/02/11/mUiAHC4s8yql51z.png)

- **Chain of Action-Thought (COAT) Reasoning**：
  - **Continue reasoning**（<|continue|>）：Encourage the model to generate the next intermediate step. 
  - **Reflect**（<|reflect|>）：Verify whether the previous reasoning steps are correct.
  - **Explore alternatives**（<|explore|>）：Identify holes in reasoning and explore new solutions. 

- **Two-stage training framework**：
  - **Small-scale format tuning phase**：Fine-tune on a small dataset with a small number of inference trajectory examples to familiarize the model with the COAT inference format. 
  - **Large-scale self-optimization stage**：Optimize model performance through reinforcement learning (RL) and use restart and exploration (RAE) technology to improve the model's autoregressive search capabilities.


### Mathematical Reasoning Benchmark of Satori-7B-Round2

In mathematical reasoning, Satori-7B-Round2 has achieved SOTA performance and outperformed Qwen-2.5-Math-7B-Instruct, which uses the same basic model (Qwen-2.5-Math-7B). It even significantly surpassed Llama-3.1-70B-Instruct, a model with ten times more parameters.

![Satori_math_reasoning](https://s2.loli.net/2025/02/13/rIdankjoPZJSNwe.png)

### Satori-7B-Round2 general domain reasoning benchmark

Satori-7B-Round2, trained only on the mathematics dataset, shows strong transfer capabilities across multiple out-of-domain reasoning benchmarks and significantly surpasses Qwen-2.5-Math-7B-Instruct.

Despite not being trained on other domains, Satori-7B-Round2 performs as well as or better than other small general-purpose instruction models and is comparable to larger models such as Llama-3.1-70B-Instruct.

![Satori_general_domain_reasoning](https://s2.loli.net/2025/02/13/k6B2KLUpwhtSmEj.png)

## Satori-7B-Round2-WebUI operating interface

![Satori-7B-Gradio](https://ibb.co/PvJCdhgm)


## Manual local deployment Satori-7B-Round2-WebUI

#### 1. Clone the project to local
```bash
git clone https://github.com/AloofWolFX/Satori-7b-round2-webui.git
cd Satori-7b-round2-webui
```

#### 2. Create a virtual environment:
```bash
python -m venv myenv
```

#### 3. Activate the virtual environment:
```bash
source myenv/bin/activate
```

#### 4. Install dependency packages:
```bash
pip install torch vllm gradio tqdm
```

#### 5. Run the program:

You can start the application in the following ways:
```bash
python gradio_app.py --share --host 0.0.0.0 --port 7860
```

Default configuration:
- Host address: 127.0.0.1
- Port: 7860
- Only local access is allowed


The program will automatically download the model file for you, and after the download is complete, it will automatically start the inference engine and Gradio App. Finally, the access address of Gradio App will be output, which is roughly as follows:
```raw
* Running on public URL: https://62c32ff6bbd7ca4d2f.gradio.live
```

## Resource

- **HuggingFace **：<https://huggingface.co/Satori-reasoning/Satori-7B-Round2>
