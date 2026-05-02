import fitz  # PyMuPDF
import numpy as np

class DocumentRetriever:
    def __init__(self):
        # 模拟加载大量企业文档，导致 Input Token 激增
        self.documents = []

    def load_document(self, file_path):
        """模拟加载一个大文档，提取文本"""
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        # 假设文档很大，这里会产生大量 Token
        return text[:100000]  # 截取部分文本模拟高 Input 场景