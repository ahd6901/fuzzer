from urllib.parse import urlparse


def parseUrl(all_links):
    for link in all_links:
        scheme= urlparse(link).scheme
        netloc = urlparse(link).netloc
        path = urlparse(link).path
        query = urlparse(link).query
        print('['+scheme+'://'+netloc+ path+', '+query + ']')

    #
    # query = urlparse('https://www.google.com/search?q=+httlp+response+elapsed+time+soup&rlz=1C1SQJL_viVN927VN927&sxsrf=APq-WBvSF2ZHGET4ja9ePq24fZbSBNg_VQ%3A1644807526590&ei=ZsUJYs2yI_inptQP3uyj4A0&ved=0ahUKEwjN_eHCmf71AhX4k4kEHV72CNwQ4dUDCA4&uact=5&oq=+httlp+response+elapsed+time+soup&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGABKBAhGGABQAFgAYIgCaABwAXgAgAFPiAFPkgEBMZgBAKABAcABAQ&sclient=gws-wiz').path
    # query = urlparse(link).query
    # print('[' + link + ', ' + query + ']')
    pass
