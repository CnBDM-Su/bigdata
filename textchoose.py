#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:44:46 2018

@author: lipeiyu
"""
 
from PIL import Image
from wordcloud import WordCloud 
from matplotlib import pyplot as plt
import numpy as np
import re

text = open('/Users/lipeiyu/Downloads/bigdata-master/nb_raw_data/2018.csv','r',encoding = 'utf-8').read()
text_choose =re.sub(' to | de |Problem|based|Based| Using | using | a | A | via | of | Of | Method | method |Two| for | For | with | With | from | on | On | in | and |New|new| Some | some | The | the | by | an | An |One |Toword|Approach|Multi |A |An |By ',' ',text)      #剔除无关信息
#a = re.findall("[^based]", text)
#con = jieba.lcut(text)     #分词
#words = " ".join(con)    #分词后插入空格

img = Image.open('/Users/lipeiyu/Downloads/timg-2.jpeg') #打开图片
img_array = np.array(img) #将图片装换为数组

#生成词云
wc = WordCloud(mask=img_array,background_color='white',scale=10)
#wc.generate(text)
wc.generate(text_choose)

#显示词云图片
plt.imshow(wc)
plt.axis('off')
plt.figure()
plt.show()  #显示图片
 
#保存图片
wc.to_file('/Users/lipeiyu/Desktop/2018_new.jpg')

f = open("/Users/lipeiyu/Desktop/text_choose_2018.csv",'a')
f.write(text_choose)  
f.close()  