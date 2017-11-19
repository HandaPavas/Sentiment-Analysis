
> git clone “https://github.com/HandaPavas/Sentiment-Analysis”

File_Parsing.py has already been compiled and article are kept at NLP_Project/Dataset

Download stanford-corenlp from below link:
https://stanfordnlp.github.io/CoreNLP/index.html#download

Open terminal and type commands as follows:
> cd stanford-corenlp
>java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

Now, open another terminal or shell and execute:
> python coreference.py 
(change the paths in file with your current location of the project)
This co-reference file results in new files with anaphora resolved.

> python NER.py 
(change the paths in file with your current location of the project)
This NER file results in new files with all the Name-Entity extracted per article.

> python Sentiment_Analysis.py 
(change the paths in file with your current location of the project)
This file generates the final plot and results claming the sentiments per article (in terms of Name-Entity) and the overall estimation.
