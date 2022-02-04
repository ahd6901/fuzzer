from urllib.parse import urlparse


def parseUrl(all_links):
    for link in all_links:
        query = urlparse(link).query
        print('[' + link + ', ' + query + ']')
    pass
