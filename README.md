# Satori-7B-Round2-Gradio

Satori-7B-Round2 是一个专注于数学问题求解的推理模型。

- **HuggingFace 仓库**：<https://huggingface.co/Satori-reasoning/Satori-7B-Round2>

基于 Satori-7B-Round2 推理模型和 Gradio API 提供了一个友好的 Web 界面，方便快速部署和体验模型的推理能力。

## 环境依赖

- Python >= 3.10
- PyTorch
- vllm
- gradio
- tqdm

## 运行步骤

1. 克隆项目到本地

2. 安装依赖包：
```bash
pip install torch vllm gradio tqdm
```

3. 运行程序：
```bash
python gradio_app.py
```
程序会自动帮你下载模型文件，下载完成后会自动启动推理引擎和 Gradio App。

4. 访问Web UI：
推理引擎初始化完成并启动后，最终会输出 Gradio App 的访问地址，大致如下：
```
* Running on local URL:  http://127.0.0.1:7860
* Running on public URL: https://62c32ff6bbd7ca4d2f.gradio.live
```

## 运行界面

![Satori-7B-Gradio](https://s2.loli.net/2025/02/11/VwUoqjbtGizNyMm.png)