#!/usr/bin/env python3

import pandas as pd

fruits = {'香蕉': 115, '梨': 79, '椰子': 241, '柿子': 74, '鲜枣': 125,
          '榴莲': 147, '石榴': 72, '菠萝蜜': 105, '牛油果': 143, '山楂': 102}
s_fruits = pd.Series(fruits)

from pyecharts.charts import Pie
from pyecharts import options as opts

# 饼图
pie = Pie(init_opts=opts.InitOpts(width='800px', height='600px', bg_color='white'))
pie.add(
    '', [list(z) for z in zip([fruit for fruit in s_fruits.index], s_fruits)], center=['50%', '50%']
).set_series_opts(
    label_opts=opts.LabelOpts(formatter="{b}: {c}"),
).set_global_opts(
    title_opts=opts.TitleOpts(title='水果的热量对比(kcal/100g)', pos_left='300', pos_top='20',
        title_textstyle_opts=opts.TextStyleOpts(color='black', font_size=16)),
    legend_opts=opts.LegendOpts(is_show=False)
).render('fruits_calorie1.html')

# 玫瑰图
pie = Pie(init_opts=opts.InitOpts(width='800px', height='600px', bg_color='white'))
pie.add(
    '', [list(z) for z in zip([fruit for fruit in s_fruits.index], s_fruits)],
    radius=['10%', '70%'], center=['50%', '50%'], rosetype="radius"
).set_series_opts(
    label_opts=opts.LabelOpts(formatter="{b}: {c}")
).set_global_opts(
    title_opts=opts.TitleOpts(title='水果的热量对比(kcal/100g)', pos_left='300', pos_top='20',
        title_textstyle_opts=opts.TextStyleOpts(color='black', font_size=16)),
    legend_opts=opts.LegendOpts(is_show=False)
).render('fruits_calorie3.html')
