from urllib.parse import urlparse


def parseUrl(all_links):
    for link in all_links:
        scheme= urlparse(link).scheme
        netloc = urlparse(link).netloc
        path = urlparse(link).path
        query = urlparse(link).query
        print('['+scheme+'://'+netloc+ path+', '+query + ']')

