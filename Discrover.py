def discover(browser, url, word_list, extension_list):
    cookies = browser.get_cookiejar()
    # page guessing
    possible_paths = []
    correct_guesses = []



    # get possible paths
    for word in word_list:
        for extension in extension_list:
            possible_paths.append('/' + word + extension)
    # Validate possible paths
    for path in possible_paths:
        full_url = url + path
        res = browser.open(full_url)
        if res.status_code == 200:
            correct_guesses.append(full_url)
    pass
