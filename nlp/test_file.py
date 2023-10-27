
# 定义一个函数，读取文本数据
def read_text(data):
    # 将每一行数据按照\t分割，并将最后一个元素去掉，将<sssss>替换为空字符，去掉空格
    text = [each.split('\t')[-1].replace('<sssss>','').strip() for each in data]
    # 将每一行数据按照\t分割，并将第三个元素转换为整数
    label = [int(each.split('\t')[-3]) for each in data]
    # 将text和label组合成列表
    data = list(zip(text, label))
    # 返回组合后的列表
    return data

with open('./train.txt') as trainfile:
    traintext = trainfile.readlines()

traindata = read_text(traintext)
print(traindata)