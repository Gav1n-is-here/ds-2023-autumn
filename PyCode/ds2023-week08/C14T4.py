import numpy as np
from sklearn.datasets import fetch_20newsgroups   #获取数据集
from sklearn.feature_extraction.text import TfidfVectorizer #TF-IDF文本特征提取
from sklearn.naive_bayes import MultinomialNB #朴素贝叶斯



train=fetch_20newsgroups(subset='train')
test=fetch_20newsgroups(subset='test')

#将文章数据向量化（TF-IDF算法）
vectorizer = TfidfVectorizer() 
train_v=vectorizer.fit_transform(train.data)
test_v=vectorizer.transform(test.data)

Classifier = [MultinomialNB()]
Classifier_str = ['MultinomialNB()']
for i in Classifier_str:
    
    model = eval(i)
    model.fit(train_v,train.target)
    print(i+"准确率为:",model.score(test_v,test.target))

