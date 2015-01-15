# -*- coding: utf-8 -*-
"""
Lee los datos de Yahoo (XML), los analiza con word2vec (gensim)

Created on Tue Jan 13 18:14:14 2015

@author: nievesabalos
"""
#import xml.etree.ElementTree as ET
import xml.etree.cElementTree as ET
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

pathData = '../data'
pathSmallData = '../datasmall'
fileToRead = '../data/FullOct2007.xml'
smallFileToRead = '../datasmall/small_sample.xml'

print "+ Fichero que voy a leer:"
print smallFileToRead
print "\nGenero un árbol para el contenido del archivo XML..."

def procesarElemento(nodoRoot):
   print "\nRecorro un elemento '<vespaadd>'..."
   for nodo in nodoRoot.findall("./document"):
       idioma = nodo.find('language').text.encode('utf8')
       print idioma
       if idioma == 'es-es':#'en-us':
           print "\nExtraigo del elemento..." 
           categoria = nodo.find('cat').text.encode('utf8')
           categoriaPrincipal = nodo.find('maincat').text.encode('utf8')
           subcategoria = nodo.find('subcat').text.encode('utf8')
           pregunta = FormatData(nodo.find('subject').text).encode('utf8')
           contenido = FormatData(nodo.find('content').text).encode('utf8')
           mejorRespuesta = FormatData(nodo.find('bestanswer').text).encode('utf8')
           otrasRespuestas = []
           for respuestas in nodo.findall('nbestanswers/answer_item'):
               otra = respuestas.text.encode('utf8')
               otrasRespuestas.append(FormatData(otra))
               
           with open('dataYahooQA.txt', 'a') as fileData:
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


tnode = ''
def process_buffer(buf):
    global tnode
    tnode = ET.fromstring(buf) # is an Element
    procesarElemento(tnode)
    #pull it apart and stick it in the database

inputbuffer = ''
with open(smallFileToRead,'rb') as inputfile:
    append = False
    for line in inputfile:
        if '<vespaadd>' in line:
            inputbuffer = line
            append = True
        elif '</vespaadd>' in line:
            inputbuffer += line
            append = False
            process_buffer(inputbuffer)
            inputbuffer = None
            del inputbuffer #probably redundant...
        elif append:
            inputbuffer += line
        


