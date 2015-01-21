wget http://dumps.wikimedia.org/eswiki/20150105/eswiki-20150105-pages-articles.xml.bz2

bzcat eswiki-20150105-pages-articles.xml.bz2 |  ./extractor/WikiExtractor.py -cb 500K -o extracted

find extracted -name '*bz2' -exec bunzip2 -c {} \; > wikipedia_es.xml

rm -rf extracted
