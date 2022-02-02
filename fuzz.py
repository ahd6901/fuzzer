import mechanicalsoup
import argparse
from Discrover import discover


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help="Commands[discover|test]")
    parser.add_argument('url', help="URL")
    parser.add_argument('--custom-auth',
                        help="Signal that the fuzzer should use hard-coded authentication for a specific application "
                             "(e.g. dvwa).")
    parser.add_argument('--common-words',
                        help='Newline-delimited file of common words to be used in page guessing. Required.')
    parser.add_argument('--extensions',
                        help="Newline-delimited file of path extensions, e.g. '.php'. Optional. Defaults to '.php'' "
                             "and the empty string if not specified")
    args = parser.parse_args()

    if args.action == 'discover' or args.action == 'test':
        pass
    else:
        exit()

    # Checks, args, gets word_list and extension_list
    if args.common_words is None:
        exit()
    word_list = read_file_content(args.common_words)
    if args.extensions is None:
        extension_list = ['.php']
    else:
        extension_list = read_file_content(args.extensions)

    #login
    browser = login(args.url)

    #discover
    discover(browser, args.url, word_list, extension_list)


def login(url):
    browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
    # Go to setup.php, submit new creat/set
    browser.open(url + 'setup.php')
    browser.select_form()
    browser.submit_selected()

    # Navigate to url, It should redirect to login.php
    browser.open(url)

    # Submit login form
    form = browser.select_form()
    browser['username'] = 'admin'
    browser['password'] = 'password'
    browser.submit_selected()

    # Set security level to easy, and submit the form
    browser.open(url + 'security.php')
    form2 = browser.select_form()
    browser['security'] = 'low'
    browser.submit_selected()

    # Return to main page. Print out its HTML to console
    browser.open(url)
    print("Logged into DVWA.")

    return browser


def read_file_content(filename):
    with open(filename) as f:
        return f.read().splitlines()


if __name__ == '__main__':
    main()
