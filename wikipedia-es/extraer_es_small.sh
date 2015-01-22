if [ ! -e eswiki-20150105-pages-articles2.xml.bz2 ]; then
    wget https://dumps.wikimedia.org/eswiki/20150105/eswiki-20150105-pages-articles2.xml.bz2 
fi

bzcat eswiki-20150105-pages-articles2.xml.bz2 | ./WikiExtractor.py -cb 500K -o extracted

find extracted -name '*bz2' -exec bunzip2 -c {} \; > wikipedia_es_small.xml

rm -rf extracted
