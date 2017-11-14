import csv
import re
content = []
with open("/home/pavas/IIITD/NLP/Project/TOI_GST.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        content.append(row[1])

'''for i in range(len(content)):
	a = (nltk.sent_tokenize(content[i]))
	a = [nltk.word_tokenize(sent) for sent in a]
	a = [nltk.pos_tag(sent) for sent in a]
'''
for i in range(len(content)):
    sentence = re.sub(r'\.([A-Z])', r'. \1', content[i])
    filename = "/home/pavas/IIITD/NLP/Project/Space_separted_File/" + str(i) +"_article.txt"
    with open(filename , "w")as f:
        f.write(sentence)
