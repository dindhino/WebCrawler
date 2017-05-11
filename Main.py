import re
import BeautifulSoup
import urllib2

regex = re.compile(
            r'^(?:http|ftp)s?://' # http://, ftp://, https://, atau ftps://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ... atau ip
            r'(?::\d+)?' #opsional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )

def isValidUrl(url):
    if regex.match(url) is not None:
        return True
    return False

def crawler(SeedUrl):
    tocrawl = [SeedUrl]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        print 'Crawled:'+page
        pagesource = urllib2.urlopen(page)
        s = pagesource.read()
        soup = BeautifulSoup.BeautifulSoup(s)
        links = soup.findAll('a', href = True)
        if page not in crawled:
            for l in links:
                if isValidUrl(l['href']):
                    tocrawl.append(l['href'])
            crawled.append(page)
    return crawled

crawler('http://telkomuniversity.ac.id')

