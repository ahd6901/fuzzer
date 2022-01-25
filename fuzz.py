import requests
import mechanicalsoup
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help="Commands[discover|test]")
    parser.add_argument('url', help="URL")
    parser.add_argument('--custom-auth',
                        help="Signal that the fuzzer should use hard-coded authentication for a specific application (e.g. dvwa).")
    args = parser.parse_args()

    # input validation
    if args.action == 'discover' or args.action == 'test':
        pass
    else:
        exit

    # Connect
    browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')

    # Go to setup.php, submit new creat/set
    browser.open(args.url + 'dvwa/setup.php')
    browser.post(args.url + 'dvwa/setup.php#')

    # Navigate to url, It should redirect to login.php
    browser.open(args.url + 'dvwa/')
    # Submit login form
    form = browser.select_form('form[action="login.php"]')
    browser['username'] = 'admin'
    browser['password'] = 'password'
    browser.submit_selected()

    # Set security level to easy, and submit the form
    browser.open(args.url + 'dvwa/security.php')
    form2 = browser.select_form('form[method="POST"]')
    browser['security'] = 'high'
    browser.submit_selected()

    # Return to main page. Print out its HTML to console
    browser.open(args.url + 'dvwa/')
    print(str(browser.get_current_page()))
    browser.launch_browser()


if __name__ == '__main__':
    main()
