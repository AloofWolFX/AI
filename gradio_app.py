import gradio as gr
from main import generate, prepare_prompt
from typing import Iterator
import re


def extract_final_answer(text: str) -> str:
    # 使用正则表达式匹配\boxed{...}中的内容
    match = re.search(r'\\boxed{([^}]*)}', text)
    if match:
        return match.group(1)
    return "未找到最终答案"


def process_question_stream(question: str, history: list = None) -> Iterator[tuple[str, str]]:
    completions = generate([prepare_prompt(question, history)])
    full_response = completions[0][0]

    # 模拟流式输出
    words = full_response.split()
    current_text = ""

    for word in words:
        current_text += word + " "
        yield current_text, extract_final_answer(current_text)


def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# Satori-7B Math Problem Solver")

        chatbot = gr.Chatbot(
            label="对话历史",
            height=400,
            show_label=True,
        )

        with gr.Row():
            with gr.Column(scale=4):
                question_input = gr.Textbox(
                    label="请输入数学问题",
                    placeholder="例如：哪个数字更大? 是 9.11 还是 9.9?",
                    lines=2
                )
            with gr.Column(scale=1):
                submit_btn = gr.Button("提交问题", variant="primary")

        final_answer = gr.Textbox(
            label="推理过程",
            lines=10,
            interactive=False
        )

        def user_input(user_message: str, history: list) -> tuple[str, list]:
            return "", history + [[user_message, None]]

        def bot_response(history: list) -> tuple[list, str]:
            # 获取除最后一个问题外的历史对话
            chat_history = history[:-1] if len(history) > 1 else None
            for response, answer in process_question_stream(history[-1][0], chat_history):
                history[-1][1] = answer  # 只在对话历史中显示最终答案
                yield history, response  # 将推理过程输出到原来的最终答案框

        question_input.submit(user_input, [question_input, chatbot], [question_input, chatbot]).then(
            bot_response, chatbot, [chatbot, final_answer]
        )

        submit_btn.click(user_input, [question_input, chatbot], [question_input, chatbot]).then(
            bot_response, chatbot, [chatbot, final_answer]
        )

    return demo


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='启动Satori-7B数学问题求解器')
    parser.add_argument('--share', action='store_true',
                        help='是否允许公网访问（默认仅允许本地访问）')
    parser.add_argument('--host', type=str, default='127.0.0.1',
                        help='服务器监听地址（默认：127.0.0.1）')
    parser.add_argument('--port', type=int, default=7860,
                        help='服务器监听端口（默认：7860）')
    args = parser.parse_args()

    demo = create_interface()
    demo.queue()
    demo.launch(share=args.share,
                server_name=args.host,
                server_port=args.port)
