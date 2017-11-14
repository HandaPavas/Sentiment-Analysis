##from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
for y in range(0, 74):
    y = str(y)
    filename = "/home/pavas/IIITD/NLP/Project/Anaphora_Resolved/"+y+"_article.txt"
    try:            
        with open(filename, "r") as f:
            text= f.read()
## NLTK NER tagger          
##        print ne_chunk(pos_tag(word_tokenize(text)))

## Stanford NER tagger uses an advanced statistical learning
## algorithm as compared to NLTK
        st = StanfordNERTagger('/home/pavas/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz','/home/pavas/stanford-ner-2017-06-09/stanford-ner.jar', encoding='utf-8')
        tokenized_text = word_tokenize(text)
        classified_text = st.tag(tokenized_text)
        filename = "/home/pavas/IIITD/NLP/Project/Name_Entity/"+y+"_article.txt"
        name_entity = []
        for i in classified_text:
            if i[1]!='O':
                if i[0] not in name_entity:
                    name_entity.append(i[0])
        with open(filename, "w") as f:
            for i in name_entity:
                f.write(i+"\n")
    except:
        print ("File no. "+y+" not found")
