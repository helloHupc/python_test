#!/usr/bin/env python3

from pyecharts import options as opts
from pyecharts.charts import Bar
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# 创建一个新的Excel文件
wb = Workbook()
ws = wb.active

# 生成Pyecharts图表
bar = (
    Bar()
    .add_xaxis(['A', 'B', 'C', 'D'])
    .add_yaxis('Series 1', [10, 20, 30, 40])
    .set_global_opts(title_opts=opts.TitleOpts(title='Bar Chart'))
)

# 渲染图表，保存为图片
chart_image = 'chart.jpg'
bar.render(chart_image)

# 将图片插入Excel中
img = Image(chart_image)
ws.add_image(img, 'E5')

# 保存Excel文件
excel_file = 'chart.xlsx'
wb.save(excel_file)