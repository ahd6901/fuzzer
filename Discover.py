from urllib.parse import urlparse, urljoin
from CrawLinks import dfs
from ParseForm import parseForm
from ParseURL import parseUrl


def discover(browser, url, word_list, extension_list):
    cookies = browser.get_cookiejar()
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

    all_links = correct_guesses.union(crawled_links)

    print("Parsed URLs (from guessed pages and discovered links) ")
    print("********************************************")
    parseUrl(all_links)


    print("Discovered Forms")
    print("********************************************")
    for link in all_links:
        parseForm(browser, link)


    print("Cookies:")
    print('*********************************************************')
    for i in cookies:
        print(i.name + ": " + i.value)
