#导入特征数值计算类（支持传入停止词）
from sklearn.feature_extraction.text import CountVectorizer
#语料
corpus = [
          'My dog has a flea problems.',
          'Maybe it is stupid to take him to a dog park.',
          'Try to prevent my dog from eating my steak.'
]

# 实例化
vectorizer = CountVectorizer()
#生成词汇表
term_frequencies = vectorizer.fit_transform(corpus) 
vocab = vectorizer.get_feature_names_out()
print(vocab)
re=vectorizer.transform(['My dog likes steak.']).toarray()
print(re)