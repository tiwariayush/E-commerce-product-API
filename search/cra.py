from webscraping import download, xpath
from urlparse import urlparse

D = download.Download()

def parse(url):

  if url.find('flipkart')>=0:
    html = D.get(url)
    item_name = xpath.get(html,'//h1[@itemprop="name"]//text()')
    item_price = xpath.get(html, '//span[@class="fk-font-verybig pprice fk-bold"]//text()')
    item_image = xpath.get(html,'//div[@class="image-wrapper"]/img/@src')

    print item_name, item_price, item_image

  else:
    html = D.get(url)
    item_name = xpath.get(html ,'//span[@id="productTitle"]//text()')
    item_price = xpath.get(html,'//span[@id="priceblock_ourprice"]//text()')
    item_image = xpath.get(html, '//div[@class="imgTagWrapper"]/img/@src')

    print item_name, item_price, item_image

