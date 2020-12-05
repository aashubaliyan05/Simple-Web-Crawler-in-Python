from typing import Final, final
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls=list()
url_extracted=list()



def crawl_url(url):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    #extracting all anchor tags
    tags = soup('a')
    extract_url(tags)


def extract_url(tags):
    #adding to list urls
    for tag in tags:
        urls.append(str(tag.get("href",None)))
    for url_filtered in urls:
        if (url_filtered.startswith("http") or url_filtered.startswith("https")):
            if(url_filtered not in url_extracted):
                print(url_filtered)
                url_extracted.append(url_filtered)
            else:
                pass

    
def spider(url_extracted):
        base_len: final = len(url_extracted)
        for spidering in range(base_len):
            url = url_extracted[spidering]
            crawl_url(url)


url=input("enter a url : ")
crawl_url(url)
spider(url_extracted)







