import sys
import csv
from urlparse import urlparse
from webscraping import download , xpath

def extract(url):

  D = download.Download()

  f = open('website.csv', 'rb')
  reader = csv.reader(f)
  row = list(reader)

  for r in range(0,3):
    if url.find(row[r][0])>=0:
      xpath1 = row[r][1]
      xpath2 = row[r][2]
      xpath3 = row[r][3]  

      html = D.get(url)
      item={}
      item['name'] = xpath.get(html,'%s//text()' % xpath1)
      item['price'] = xpath.get(html,'%s//text()' % xpath2)
      item['image'] = xpath.get(html, '%s' % xpath3)

      print item

if __name__ == '__main__':
   url="".join( sys.argv[1:] )
   extract(url)