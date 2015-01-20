# -*- coding: utf-8 -*-
"""
Los datos de Yahoo (txt), los analiza con word2vec (gensim)

Created on Tue Jan 13 18:14:14 2015

@author: nievesabalos
"""
import re, unicodedata
from gensim import models
import logging, os, sys
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

fileToRead = './es_dataYahooQA.txt'
fileModel = 'es_modelYahooQA.model'
fileModelBin = 'es_modelYahooQA.model.bin'
fileModelTxt = 'es_modelYahooQA.model.txt'

program = os.path.basename(sys.argv[0])
# ---------------------------------------------------
# 1. INPUT DATA
print "Fichero:"
print fileToRead

sentences = []
with open(fileToRead, 'r') as fileData:
    for line in fileData:
        #Formatear linea si hace falta aquí
        line = line.lower()
        line = line.decode('utf-8')
        line = unicodedata.normalize('NFKD', line).encode('ascii','ignore').lower()
        line = re.sub('[\n/:.!,;)()-_?]', '', line)
        if len(line) > 1:
            sentences.append(line.split(" "))
        
    print "Cierro fichero."
    fileData.close()

print "\nFrases a analizar con word2vec:"             
print len(sentences)
#print sentences[0:100]
# ---------------------------------------------------
# 2. CREATE MODEL
# train word2vec 
# parametros por defecto:
# size=100, alpha=0.025, window=5, min_count=5, sample=0, seed=1, workers=1, 
# min_alpha=0.0001, sg=1, hs=1, negative=0, cbow_mean=0, hashfxn=<built-in function hash>,
# iter=1
print "\nCreo modelo word2vec:"   
model = models.Word2Vec(sentences, size=200)

# ---------------------------------------------------
# 3. EVALUATION
# Google have released their testing set of about 20,000 syntactic and semantic 
# test examples, following the “A is to B as C is to D” task:
# model.accuracy('/tmp/questions-words.txt')



# ---------------------------------------------------
# 4. SAVE MODEL
print "\nGuardo el modelo en .model:"  
print fileModel 
model.save(fileModel)
print "\nGuardo el modelo en .bin:"  
print fileModelBin 
model.save_word2vec_format(fileModelBin, binary=True)
print "\n...y guardo el modelo en .txt:"  
print fileModelTxt 
model.save_word2vec_format(fileModelTxt, binary=False)

logging.info("finished running %s" % program)