from urllib.parse import urljoin


def dfs(browser, current_url, crawled_links, base_url):
    browser.open(current_url)
    children_links = get_children_links(browser, crawled_links, base_url)
    crawled_links.add(current_url)

    print(current_url)
    if len(children_links) != 0:
        for child_link in children_links:
            if child_link in crawled_links:
                continue
            else:

                dfs(browser, child_link, crawled_links, base_url)


def get_children_links(browser, crawled_links, base_url):
    links = []
    raw_links = browser.page.find_all('a', href=True)

    if len(raw_links) > 0:
        for raw_url in raw_links:

            absolute_url= str(urljoin(base_url, raw_url['href']))
            if base_url not in absolute_url or 'logout.php' in absolute_url:
                continue
            res = browser.open(absolute_url)

            if browser.page is None:
                continue
            if res.status_code == 200 and absolute_url not in crawled_links:
                links.append(absolute_url)

    return links
