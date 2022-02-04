from urllib.parse import urlparse, urljoin
from CrawLinks import dfs
from ParseForm import parseForm
from ParseURL import parseUrl


def discover(browser, url, word_list, extension_list):
    cookies = browser.get_cookiejar()
    for i in cookies:
        print(i.name + ": " + i.value)
    # page guessing
    possible_paths = []
    correct_guesses = set({})

    # links Crawling
    crawled_links = set({})  # set of crawled_links


    # Display results
    print("Links Discovered:")
    print("********************************************")
    dfs(browser, url, crawled_links, url)

    print("Pages Successfully Guessed:")
    print("********************************************")
    # get possible paths
    for word in word_list:
        for extension in extension_list:
            possible_paths.append(word + extension)
    # Validate possible pages
    for path in possible_paths:
        full_url = urljoin(url, path)
        res = browser.open(full_url)
        if res.status_code == 200:
            correct_guesses.add(full_url)
            print(full_url)
    print("Parsed URLs (from guessed pages and discovered links) ")
    print("********************************************")
    # TODO
    all_links = correct_guesses.union(crawled_links)


    print("Discovered Forms")
    print("********************************************")
    # TODO: page_name
    # TODO: its input's name and value

    print("Cookies:")
    print('*********************************************************')
    for i in cookies:
        print(i.name + ": " + i.value)
