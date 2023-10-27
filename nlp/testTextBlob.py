from textblob import TextBlob

# 示例文本
text = "这个产品非常出色！"

# 创建TextBlob对象
blob = TextBlob(text)

# 获取情感分析得分
sentiment = blob.sentiment

# 输出情感分析结果
print(sentiment)
