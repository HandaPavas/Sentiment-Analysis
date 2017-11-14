from pycorenlp import StanfordCoreNLP
import re
import codecs

nlp = StanfordCoreNLP('http://localhost:9000')
##text=('If they are angry about music, the neighbours will call the cops. Jack asked Jill to take him up the hill, but he refused him.')
for y in range(0,1):
    y = str(y)
    print (y)
    try:
        filename = "/home/pavas/IIITD/NLP/Project/Space_separted_File/"+y+"_article.txt"
        with open(filename, "r") as f:
            text = f.read()
        output = nlp.annotate(text,properties={'annotators':'coref','outputFormat': 'json'})
    ##  results describe the sentenceNum, startindex, endindex, text to be replaced
        results=[]
        
    ## Anaphora detection per article       
        for i in output['corefs']:
            index = 0
            for j in range(0,len(output['corefs'][i])):
                if output['corefs'][i][j]['isRepresentativeMention']==True:
                    index = j
                    break
        
            for j in range(0,len(output['corefs'][i])):
                if output['corefs'][i][j]['isRepresentativeMention']==False:
                    temp=[]
                    temp.append(output['corefs'][i][j]['sentNum'])
                    temp.append(output['corefs'][i][j]['startIndex'])
                    temp.append(output['corefs'][i][j]['headIndex'])
                    temp.append(output['corefs'][i][index]['text'])
                    results.append(temp)
    ##        print(i)
        
            
    ## Tokenize the whole article
        para = []
        for i in output['sentences']:
            sen=[]
            for j in i['tokens']:
                sen.append(j['word'])
            para.append(sen)
            
    ## Resolving anaphoras    
        for i in results:
    ##        print (i)
            sennum = i[0]
            start = i[1]
            end = i[2]
            text = i[3]
            para[sennum-1][start-1]=text
            if start != end:
                for j in range(start, end):
                    para[sennum-1][j] = ""
        

    ## Writing articles with anaphora resolved to new file
        filename = "/home/pavas/IIITD/NLP/Project/Anaphora_Resolved/"+y+"_article.txt"
        with open(filename, "w") as f:
            for sen in para:
                str1 = " ".join(sen)
                f.write(str1)

    except:
        print ("Error while resolving in file "+y)
                    


    
        
        
        
        
    
