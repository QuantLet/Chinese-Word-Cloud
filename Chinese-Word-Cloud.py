import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import PIL.Image as image
import numpy as np
import re
from nltk.corpus import stopwords
import os
from os import path
from matplotlib.colors import LinearSegmentedColormap


#first word cloud
print("dealing with word cloud 1...")
with open('sample1.txt') as fp:
    text=fp.read()


wl_space_split = list(jieba.cut(text))


sw=set(STOPWORDS)
sw.add('的')
sw.add('和')
sw.add('是')
sw.add('与')
sw.add('之间')
sw.add('以及')
sw.add('在')
sw.add('了')
sw.add('可以')
sw.add('称为')
sw.add('问题')
sw.add('将')
sw.add('进行')
sw.add('一个')
sw.add('上')
sw.add('举例')
sw.add('中')
mask=np.array(image.open("cur.jpg"))

#Hiragino Sans GB.ttc ，PingFang.ttc，STHeiti Light.ttc，STHeiti Medium.ttc
image_colors=ImageColorGenerator(mask)
cloud_=WordCloud(background_color=None,mode="RGBA",width=1000,height=1000,color_func=image_colors ,
                 mask=mask,font_path='font1.ttf',stopwords=sw,relative_scaling=1.0,
                 collocations=False,min_font_size=10,max_font_size=1000)
cloud_.generate(" ".join(wl_space_split))

plt.xticks([])
plt.yticks([])
plt.imshow(cloud_)
plt.show()

#second word cloud
print("dealing with word cloud 2...")
colors = [(179/255, 89/255, 82/255), (253/255, 207/255, 49/255), (118/255, 160/255, 191/255)]
cm2 = LinearSegmentedColormap.from_list('my_cmap2', colors, N=500)

graph = np.array(image.open('Marx.jpg'))
colors = ImageColorGenerator(graph)
with open('TheCommunistManifesto.txt', 'r', encoding='UTF-8') as file:
    rawdata = file.read()
mytext = " ".join(jieba.cut_for_search(rawdata))

stopwords = set()
temp_content = [line.strip() for line in open(r'baidu_stopwords.txt','r', encoding='UTF-8').readlines()]
stopwords.update(temp_content)
dict = {}
for key in mytext.split(' '):
    if '\n' not in key and len(key)>1:
    # print(key)
        dict[key] = dict.get(key, 0) + 1
        
wc = WordCloud(max_words=500, mode='RGBA', background_color=None,
               colormap=cm2,
            #    scale=4,
               font_path=r"font2.ttf", 
               stopwords=stopwords,
               mask=graph
               ).fit_words(dict)

fig, ax = plt.subplots(nrows=1, ncols= 1, sharex= True, dpi=300, figsize=(8, 8))
ax.imshow(wc, interpolation='bilinear')
ax.axis("off")
plt.savefig("wordcloud_abstract1.png", dpi=300, transparent=True)
plt.show()

