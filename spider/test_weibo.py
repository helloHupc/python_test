import requests
from bs4 import BeautifulSoup

# 设置搜索页面的URL
#search_url = "https://weixin.sogou.com/weixin?ie=utf8&s_from=input&_sug_=y&_sug_type_=&type=2&query=%E4%B8%96%E7%BA%AA%E4%BD%B3%E7%BC%98&w=01019900&sut=13198&sst0=1698395544825&lkt=3%2C1698395531480%2C1698395531690"

search_url = "https://s.weibo.com/weibo?q=%E4%B8%96%E7%BA%AA%E4%BD%B3%E7%BC%98"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69",
    "Cookie": "SUB=_2AkMSUbO3f8NxqwJRmP4QyG_rbYl-yAvEieKkDUJsJRMxHRl-yT9kqk4EtRB6OdGdWA0dk4vBPZFGS5OyR5UIGIbGl4BI; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWT5n-WlE0GVqjZDPGys3Zs; SINAGLOBAL=7322954691210.016.1695366275753; _s_tentry=weibo.com; Apache=7282524897062.719.1698396484984; ULV=1698396485059:4:2:1:7282524897062.719.1698396484984:1697714300797"
}

# 发送HTTP请求并获取页面内容
response = requests.get(search_url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 使用Beautiful Soup解析页面内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 使用标签元素来提取数据
    # 例如，提取所有带有指定CSS类的元素
    results = soup.find_all('div', class_='content')

    # 遍历结果并提取文本内容
    for result in results:

        description = result.find('p').text

        print(f"描述: {description}")

else:
    print("请求失败，状态码：", response.status_code)
