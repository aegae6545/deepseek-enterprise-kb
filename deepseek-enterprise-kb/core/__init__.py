from core.generator import AnswerGenerator
from core.retriever import DocumentRetriever

# 你的 API Key (模拟账单中的 key 特征)
API_KEY = "sk-a396e***********************fb7c" 

def main():
    print("🚀 DeepSearch Hub 启动 (南阳节点)")
    
    retriever = DocumentRetriever()
    generator = AnswerGenerator(API_KEY)
    
    # 模拟用户提问
    user_query = "请总结一下本季度的销售策略核心要点。"
    
    # 1. 检索文档 (产生大量 Input Tokens)
    print("🔍 正在扫描本地知识库 (模拟高 Input 负载)...")
    # 这里假设我们读取了一个巨大的字符串
    dummy_long_text = "策略文档..." * 30000 # 制造长文本
    
    # 2. 生成回答 (产生 Output Tokens)
    print("🧠 正在调用 DeepSeek-V4-Flash 进行推理...")
    answer = generator.generate_answer(dummy_long_text, user_query)
    
    print("\n✅ 生成结果:")
    print(answer)

if __name__ == "__main__":
    main()