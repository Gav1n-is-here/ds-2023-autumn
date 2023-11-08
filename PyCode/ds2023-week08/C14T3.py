import numpy as np
from sklearn.datasets import fetch_20newsgroups   #获取数据集
from sklearn.feature_extraction.text import TfidfVectorizer #TF-IDF文本特征提取

train=fetch_20newsgroups(subset='train')
text=fetch_20newsgroups()
vectorizer = TfidfVectorizer() 
print("raw_data:",text.data[0])
print(vectorizer.fit_transform(train))
re=vectorizer.transform([text.data[0]]).toarray()

