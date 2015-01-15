# -*- coding: utf-8 -*-
"""
Lee los datos de Yahoo (XML), los analiza con word2vec (gensim)

Created on Tue Jan 13 18:14:14 2015

@author: nievesabalos
"""
import xml.etree.ElementTree as ET
import HTMLParser
import logging, os
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# preprocess the words from the files — convert to unicode, lowercase, remove 
# numbers, extract named entities… All of this can be done 
# inside the MySentences iterator and word2vec doesn’t need to know.
h = HTMLParser.HTMLParser()
def FormatData(line):
    #print("Formateo la frase:"+line)
    fraseLimpia = h.unescape(line)
    saltoDeCarro = '<br />'
    repeticiones = fraseLimpia.count(saltoDeCarro)
    #print repeticiones
    if repeticiones != 0:
        fraseLimpia = fraseLimpia.replace(saltoDeCarro, "", repeticiones)
    return fraseLimpia

#contadorSpanish = 0
#def FindSpanish(line):
#    words = line.split()
#    for word in words:
#        if len(word) > 6 and word[0:7] == '<qlang>':
#            if word == '<qlang>es</qlang>':
#               global contadorSpanish
#               contadorSpanish = contadorSpanish + 1
               #print line
#               return 1

# Gensim only requires that the input must provide sentences sequentially,
# when iterated over. No need to keep everything in RAM: we can 
# provide one sentence, process it, forget it, load another sentence… 
# if our input is strewn across several files on disk, with one sentence per line:
#class MySentences(object):
#    def __init__(self, dirname):
#        self.dirname = dirname

#    def __iter__(self):
#        for fname in os.listdir(self.dirname):
#            if os.path.isfile(os.path.join(self.dirname, fname)):
#               for line in open(os.path.join(self.dirname, fname)):
#                   #llamar a la función que limpia antes
#                   FindSpanish(line)
#                   yield line.split()
                
#    def __str__(self):
#        print "Ruta donde leo los datos:"
#        return self.dirname

#pathData = '../datasmall'
pathData = '../data'
pathSmallData = '../datasmall'
#compruebo que sean correctos los ficheros de entrada
print "+ Carpetas que voy a leer:"
print(os.listdir(pathData))

fileToRead = '../data/FullOct2007.xml'
smallFileToRead = '../datasmall/small_sample.xml'

print "+ Fichero que voy a leer:"
print fileToRead
print "\nGenero un árbol para el contenido del archivo XML..."
tree = ET.parse(fileToRead)
root = tree.getroot()
print(root.tag, root.attrib)

print "\nRecorro el árbol buscando items vespaadd/document..."
for bloqueQA in root.findall("./vespaadd/document"):
   #print '\n**************************************************************'
   #print(bloqueQA.tag, bloqueQA.attrib)
   idioma = bloqueQA.find('language').text.encode('utf8')
   print idioma
   if idioma == 'es-es':
       print "\nElemento en castellano. No hago nada" 
       categoria = bloqueQA.find('cat').text.encode('utf8')
       categoriaPrincipal = bloqueQA.find('maincat').text.encode('utf8')
       subcategoria = bloqueQA.find('subcat').text.encode('utf8')
       pregunta = FormatData(bloqueQA.find('subject').text).encode('utf8')
       contenido = FormatData(bloqueQA.find('content').text).encode('utf8')
       mejorRespuesta = FormatData(bloqueQA.find('bestanswer').text).encode('utf8')
       otrasRespuestas = []
       for respuestas in bloqueQA.findall('nbestanswers/answer_item'):
           otra = respuestas.text.encode('utf8')
           otrasRespuestas.append(FormatData(otra))
           
       with open('dataSpanish.txt', 'a') as fileData:
         print "Escribo en fichero pregunta y respuestas sobre:"
         print pregunta
         fileData.write('\nCATEGORÍA\n')
         fileData.write(categoria)
         fileData.write('\nCATEGORÍA PRINCIPAL\n')
         fileData.write(categoriaPrincipal)
         fileData.write('\nSUBCATEGORÍA\n')
         fileData.write(subcategoria)
         fileData.write('\nPREGUNTA\n')
         fileData.write(pregunta)
         fileData.write('\nCONTENIDO\n')
         fileData.write(contenido)
         fileData.write('\nMEJOR RESPUESTA\n')
         fileData.write(mejorRespuesta)
         fileData.write('\nOTRAS RESPUESTAS\n')
         for respuestas in otrasRespuestas:
             fileData.write(respuestas) 
             fileData.write('\n')
             
         print "Cierro fichero."
         fileData.close()
   #else:
       # print "\nElemento en inglés... obtengo los elementos con texto."
       # if idioma == 'en-us':
 
# Lo que dentro de pathData sea un directorio no lo leo, sólo leo ficheros
#sentences = MySentences(pathData) # a memory-friendly iterator
#print(sentences)

#count = 0
# Si quiero ver lo que hay en sentences:
#for i in sentences:
#   count = count + 1

#print "Frases total:"
#print count
#print "Elementos en castellano:"
#print contadorSpanish
#model = gensim.models.Word2Vec(sentences)