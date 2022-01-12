import json
import requests
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # 可视化包

url_header = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv19450&productId=100003060627&score=0&sortType=5&page="
# 切割后第二部分
url_tail = "&pageSize=10&isShadowSku=0&rid=0&fold=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

for page in range(20):
    url_tail = "&pageSize=10&isShadowSku=0&rid=0&fold=1"
    # 拼接得到最终url,并请求数据(得到键值对格式(字典)的数据)
    url_mate20 = url_header + str(page + 1) + url_tail
    res = requests.get(url_mate20, headers=headers)
    # 用json.loads将数据转化格式为json格式
    data = json.loads(res.text[27:-2])
    comment = (data['comments'])

    # 将数据遍历保存到本地的.txt文件中,
    for i in comment:
        # 注意带参数"a"，如果是w就会覆盖原有内容，这样子你只能得一条评论
        honor20i_text = open('D:\pcopt\data\honor20i_text.txt', 'a')
        honor20i_text.write('%s\n' % i['content'])
        honor20i_text.close()

# 读取爬虫保存的下载数据
file_text = open('D:\pcopt\data\honor20i_text.txt', 'r').read()

# 再使用jieba来处理剪切我们爬取文本内容
cut_text = jieba.cut(file_text)

# 继续处理对剪过的文本以空格拼接起来，注意一下这里“”有空格的
result = " ".join(cut_text)
wc_cloud = WordCloud(
    font_path='D:\pcopt\data\syl.ttf\HYQiHeiY2-75W.ttf',  # 字体的路径
    background_color='black',  # 背景颜色
    width=1200,
    height=600,
    max_font_size=150,  # 字体的大小
    min_font_size=30,  # 字体的大小
    max_words=10000
)

wc_cloud.generate(result)
wc_cloud.to_file('D:\pcopt\dataLingDucloud.png')  # 图片保存
# 图片展示
plt.figure('凌度img')  # 图片显示的名字
plt.title('JD_mate20')
plt.imshow(wc_cloud)
plt.axis('off')
plt.show()