crawled_links = set({'http://localhost/dvwa/logout.php'})  # set of crawled_links


def discover(browser, url, word_list, extension_list):
    cookies = browser.get_cookiejar()
    # page guessing
    possible_paths = []
    correct_guesses = []

    # links Crawling
    dfs(browser, url)
    print("Links Discovered:")
    print("********************************************")
    for link in crawled_links:
        print(link)
    print("Pages Successfully Guessed:")
    print("********************************************")
    # get possible paths
    for word in word_list:
        for extension in extension_list:
            possible_paths.append('/' + word + extension)
    # Validate possible pages
    for path in possible_paths:
        full_url = url + path
        res = browser.open(full_url)
        if res.status_code == 200:
            correct_guesses.append(full_url)
            print(full_url)


def dfs(browser, current_url):
    children_links = get_children_links(browser, current_url)
    crawled_links.add(current_url)
    if len(children_links) != 0:
        for child_link in children_links:
            if child_link in crawled_links:
                continue
            else:
                browser.open(child_link)
                dfs(browser, child_link)


def get_children_links(browser, url):
    links = []
    raw_links = browser.page.find_all('a', href=True)
    if len(raw_links) > 0:
        for raw_url in raw_links:
            link = browser.absolute_url(raw_url['href'])
            # if link inside domain
            if url in link:
                links.append(link)
    return links
