import pandas as pd

html = "https://mobile.anjuke.com/xf/fj-nn/2020/"
#html = "https://weixin.sogou.com/weixin?ie=utf8&s_from=input&_sug_=y&_sug_type_=&type=2&query=%E4%B8%96%E7%BA%AA%E4%BD%B3%E7%BC%98&w=01019900&sut=13198&sst0=1698395544825&lkt=3%2C1698395531480%2C1698395531690"
data = pd.read_html(html)
print(data)
