"""在 predict 中实现你的提示词与模型调用流程。"""


def predict(pair, examples, llm):
    """根据当前论文对返回字符串 "A" 或 "B"。

    pair: paper_a、paper_b 各含 title、abstract、date。
    examples: 100 条示例，另含 id 和 answer。
    llm.chat(messages): 接收消息列表，返回 content 和 reasoning。
    """
    raise ValueError("请先实现 predict 函数，再运行实验。")
