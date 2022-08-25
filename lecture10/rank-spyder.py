# -*- coding=utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 获取整个网页内容
text = urlopen('https://www.shanghairanking.cn//rankings/bcur/2022.html').read()
soup = BeautifulSoup(text, 'html.parser')
rk_table = BeautifulSoup(str(soup.find_all('tbody'))[1:-1], 'html.parser')  # 去除头尾的列表括号[]
# 调试用，检查网页标签结构
# with open('rk-table.html', 'wb') as f:
#     f.write(str(rk_table).encode('utf-8'))

school_name = []
school_tag = []
# 获取学校名称
for name in rk_table.find_all(name='a', class_='name-cn'):
    school_name.append(name.string.encode('utf-8').decode('utf-8'))
# 获取排名和分数
for tag in rk_table.find_all(name='td'):
    # 数据清洗
    try:
        school_tag.append(tag.string.strip())  # 去除前后空字符
    except AttributeError:  # 部分 td 标签无内容或嵌套，舍弃
        pass

with open('school-ranking.txt', 'w', encoding='utf-8') as f:
    f.write('%2s\t%12s\t%8s\n' % ('排名', '学校名称', '总分'))
    for index, name in enumerate(school_name):
        f.write('%2s\t%14s\t%6s\n' % (school_tag[index * 3], name, school_tag[index * 3 + 1]))
