from webscraping import download, xpath
from urlparse import urlparse

D = download.Download()

def parse(url):

  if url.find('flipkart')>=0:
    html = D.get(url)
# Downloads the whole page cache and save in webscraping log and then scrape data from it
    item={}
    import pdb; pdb.set_trace;
    item['name'] = xpath.get(html,'//h1[@itemprop="name"]//text()')
    item['price'] = xpath.get(html, '//span[@class="fk-font-verybig pprice fk-bold"]//text()')
    item['image'] = xpath.get(html,'//div[@class="image-wrapper"]/img/@src')

    return item    

  else:
    html = D.get(url)
    item={}
    item['name'] = xpath.get(html ,'//span[@id="productTitle"]//text()')
    item['price'] = xpath.get(html,'//span[@id="priceblock_ourprice"]//text()')
    item['image'] = xpath.get(html, '//div[@class="imgTagWrapper"]/img/@src')

    return item
