# -*- coding: utf-8 -*-
"""
Los datos de Yahoo (txt), los analiza con word2vec (gensim)

Created on Tue Jan 13 18:14:14 2015

@author: nievesabalos
"""
import re
import unicodedata
import logging, os, sys, string
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

minifileToRead = './es_mini_dataYahoo.txt'
fileToRead = 'es_dataYahooQA.txt'

program = os.path.basename(sys.argv[0])
# ---------------------------------------------------
# 1. INPUT DATA
print "Fichero:"
print fileToRead

def clean(x):
   x = unicodedata.normalize('NFKD', x).encode('ascii','ignore').lower()
   replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
   x = x.translate(replace_punctuation)
   x = re.sub('@%$&[\n/:!,;)()_?¿¡<>]', ' ', x)
   x = re.sub(' - ', ' ', x)
   x = re.sub(' +',' ', x).strip()
   return x
    
sentences = []
with open(fileToRead, 'r') as fileData:
    for lineas in fileData:
        #Formatear linea si hace falta aquí
        lineArray = lineas.split(".")
        for line in lineArray:
            if len(line) > 1:
                line = line.decode('utf-8')
                line = clean(line) # ¿? problemas con gensim y tildes y eñes...
                if len(line) > 1:
                    sentences.append(line.split(" "))
       
    print "Cierro fichero."
    fileData.close()

print "\n1 ++++ Frases:"             
print len(sentences)
print sentences[500:650]

logging.info("finished running %s" % program)