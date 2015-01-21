# -*- coding: utf-8 -*-
"""
Los datos de Yahoo (txt), los analiza con word2vec (gensim)

Created on Tue Jan 13 18:14:14 2015

@author: nievesabalos
"""
from gensim import models
import logging, os, sys
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#fileToRead = './es_dataYahooQA.txt'
fileModel = 'es_modelYahooQA.model'
fileModelBin = 'es_modelYahooQA.model.bin'

program = os.path.basename(sys.argv[0])
# ---------------------------------------------------
# 1. LOAD MODEL DATA
print "Fichero con el modelo:"
print fileModel

print "Modelo cargado .model:"
model = models.Word2Vec.load(fileModel) 
#print "Modelo cargado .bin:"
#model = models.Word2Vec.load_word2vec_format(fileModelBin, binary=True)
 

#print "Accuracy (vs questions-words):"
#accuracy = model.accuracy('../evaluation/questions-words.txt')
#print accuracy
 
# ---------------------------------------------------
# 2. TAREAS

print "\nTAREAS:"   


#print "\nLa palabra que no encaja en.. desayuno cereales coche leche tostada:"  
#no_encaja = model.doesnt_match("desayuno cereales coche leche tostada".split())
#print no_encaja

print "\nSimilitud entre:pregunta y novio"  
similitud = model.similarity('pregunta', 'novio')
print similitud

print "\nMás similiar a: humanidades"  
similitud = model.most_similar([u'humanidades'], topn=5)
print similitud
print "\nMás similiar a: alemania"  
similitud = model.most_similar([u'alemania'], topn=5)
print similitud
print "\nMás similiar a: novio"  
similitud = model.most_similar([u'novio'], topn=5)
print similitud
print "\nMás similiar a: coche"  
similitud = model.most_similar([u'coche'], topn=5)
print similitud
print "\nMás similiar a: telecinco"  
similitud = model.most_similar([u'telecinco'], topn=5)
print similitud

print "\nMás similiar a: religion"  
similitud = model.most_similar([u'religion'], topn=5)
print similitud
print "\nMás similiar a: relaciones"  
similitud = model.most_similar([u'relaciones'], topn=5)
print similitud

print "\nMás similiar a: categoria"  
similitud = model.most_similar([u'categoria'], topn=5)
print similitud
print "\nMás similiar a: subcategoria"  
similitud = model.most_similar([u'subcategoria'], topn=5)
print similitud
print "\nMás similiar a: idioma"  
similitud = model.most_similar([u'idioma'], topn=5)
print similitud
print "\nMás similiar a: pregunta"  
similitud = model.most_similar([u'pregunta'], topn=5)
print similitud

print "\nMás similar entre pareja y novio que no se parezca a hombre:"  
mas_similar = model.most_similar(positive=['pareja', 'novio'], negative=['hombre'])
print mas_similar

print "\nMás similar entre religion y hombre:"  
mas_similar = model.most_similar(positive=['religion', 'hombre'])
print mas_similar

print "\nWord vector de pregunta:"  
vector = model['pregunta']  # raw numpy vector of a word
print vector

logging.info("finished running %s" % program)