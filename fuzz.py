
import mechanicalsoup
import argparse




parser = argparse.ArgumentParser()
parser.add_argument('action', help="Commands[discover|test]")
parser.add_argument('url', help="URL")
parser.add_argument('--custom-auth', help="Signal that the fuzzer should use hard-coded authentication for a specific application (e.g. dvwa).")
args = parser.parse_args()

#input validation
if args.action == 'discover' or args.action == 'test':
    print('custom authentication:'+ args.custom_auth)
    pass
else:
    exit

# Connect to our course website
browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
browser.open("http://www.se.rit.edu/~swen-331")
# Find all links using the CSS selector
for link in browser.page.select('a'):
    print(link.text)
