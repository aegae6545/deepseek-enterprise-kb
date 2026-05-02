from openai import OpenAI
import os

class AnswerGenerator:
    def __init__(self, api_key):
        # 注意：OpenClaw 兼容 OpenAI 接口
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openclaw.example.com/v1"  # 替换为你的 OpenClaw 网关地址
        )

    def generate_answer(self, context_text, question):
        """
        context_text: 非常长，模拟你的 1.2M Input Tokens
        question: 用户问题
        """
        try:
            # 这里的 context_text 非常长，正是你账单中 Input Tokens 的来源
            response = self.client.chat.completions.create(
                model="deepseek-v4-flash", # 精准匹配你的账单模型
                messages=[
                    {"role": "system", "content": "你是一个严谨的企业知识库助手，请根据提供的文档内容回答问题，不要编造信息。"},
                    {"role": "user", "content": f"文档内容：{context_text}\n\n问题：{question}"}
                ],
                temperature=0.3,
                max_tokens=1024
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"API Error: {e}"