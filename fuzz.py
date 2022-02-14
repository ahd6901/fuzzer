from urllib.parse import urlparse, urljoin

import mechanicalsoup
import argparse
from Discover import discover
from Test import test


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help="Commands[discover|test]")
    parser.add_argument('url', help="URL")
    parser.add_argument('--custom-auth',
                        help="Signal that the fuzzer should use hard-coded authentication for a specific application "
                             "(e.g. dvwa).")
    # DISCOVER
    parser.add_argument('--common-words',
                        help='Newline-delimited file of common words to be used in page guessing. Required.',
                        required=True)
    parser.add_argument('--extensions',
                        help="Newline-delimited file of path extensions, e.g. '.php'. Optional. Defaults to '.php'' "
                             "and the empty string if not specified")
    # TEST
    parser.add_argument('--vectors', help="Newline-delimited file of common exploits to vulnerabilities. Required",
                        type=str)
    parser.add_argument('--sanitized-chars',
                        help="Newline-delimited file of characters that should be sanitized from inputs. Defaults to "
                             "just < and >", type=str)
    parser.add_argument('--sensitive', help="Newline-delimited file data that should never be leaked. It's assumed "
                                            "that this data is in the application's database (e.g. test data), "
                                            "but is not reported in any response. Required.", type=str)
    parser.add_argument('--slow', help="Number of milliseconds considered when a response is considered 'slow'. "
                                       "Optional. Default is 500 milliseconds", type=int, default=500)
    args = parser.parse_args()

    if args.action == 'discover' or args.action == 'test':
        pass
    else:
        exit()

    # check both test & discover required args
    if args.common_words is None:
        exit()
    word_list = read_file_content(args.common_words)
    if args.extensions is None:
        extension_list = ['.php']
    else:
        extension_list = read_file_content(args.extensions)

    # check for test specific required args
    if args.action == 'test':
        if args.vectors is None:
            print('vector list is required')
            exit()
        vectors = read_file_content(args.vectors)
        if args.sanitized_chars is None:
            sanitized = ['<', '>']
        else:
            sanitized = read_file_content(args.sanitized_chars)
        if args.sensitive is None:
            print('sensitive chars required')
            exit()
        sensitive = read_file_content(args.sensitive)
        slow = args.slow
        print("vectors=>:" + str(vectors))
        print("sanitized=>:" + str(sanitized))
        print("sensitive=>:" + str(sensitive))
        print("sensitive=>:" + str(slow))

    # check for custom-auth, gets Browser
    if args.custom_auth is None:
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(args.url)
    else:
        browser = login(args.url)

    # run discover
    discover(browser, args.url, word_list, extension_list)


def login(url):
    browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
    # Go to setup.php, submit new create/set

    browser.open(urljoin(url, 'setup.php'))
    print(str(urljoin(url, 'setup.php')))
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
    browser.open(urljoin(url, 'security.php'))
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
