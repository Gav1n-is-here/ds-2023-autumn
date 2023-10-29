def getText():
    txt = open("ds2023-week06\paper.txt", 'r',encoding='gb18030',errors = 'ignore').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, ' ')  # 将文本中的特殊字符替换为空格
    return txt


paperTxt = getText()
words = paperTxt.split()
counts = {} 
for word in words:
    counts[word] = counts.get(word, 0) + 1  
items = list(counts.items())  
items.sort(key=lambda x: x[1], reverse=True) 
for i in range(20):
    word, count = items[i]
    print("{0:<20}{1:>5}".format(word, count)) 