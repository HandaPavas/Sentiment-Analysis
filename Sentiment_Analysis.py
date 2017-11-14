import nltk
import plotly
from plotly.graph_objs import Scatter, Layout
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')
article_emotions=[]
article_no =[]
for y in range(1, 74):
    y = str(y)
    filename ="/home/pavas/IIITD/NLP/Project/Anaphora_Resolved/"+y+"_article.txt"
    try:
        with open(filename, "r")as f:
            text = f.read()
        output = nlp.annotate(text,properties={'annotators':'ssplit','outputFormat': 'json'})
        name = "Article_"+y
        print (name)
        article_no.append(name)
        para = []
        for i in output['sentences']:
            sen=[]
            for j in i['tokens']:
                sen.append(j['word'])
            para.append(sen)
##      emotion list resembles the polarity scores of each entity pair
##      of an article            
        emotion = []
        entity_pair = []
        filename ="/home/pavas/IIITD/NLP/Project/Name_Entity/"+y+"_article.txt"
        with open(filename, "r")as f:
            text = f.read().split("\n")
        text = text[0:len(text)-1]
        
        for i in range(0, len(text)):
            for j in range(i+1, len(text)):
                temp_sent =[]
##              entity_emotion list resembles the polarity scores of each sentences
##              corresponding to an entity pair
                entity_emotion =[]
                entity_pair.append(text[i]+"_"+text[j])
                for k in para:
                    if text[i] in k or text[j] in k:
                        temp_sent.append(" ".join(k))
##                print(temp_sent)
                sid = SentimentIntensityAnalyzer()
                for sentence in temp_sent:
                    ss = sid.polarity_scores(sentence)
                    entity_emotion.append(ss['compound'])
##                print(entity_emotion)
                norm_factor = len(entity_emotion)
                emotion.append(sum([x for x in entity_emotion])/norm_factor)
        plotly.offline.plot({"data": [Scatter(x=entity_pair, y=emotion)],"layout": Layout(title="Sentiment Per Article")})
        normalising_factor = len(emotion)
        article_emotions.append(sum([x for x in emotion])/normalising_factor)
                
    except:
        print("File "+y+" not found")

plotly.offline.plot({"data": [Scatter(x=article_no, y=article_emotions)],"layout": Layout(title="Overall Sentiment")})
        
        
