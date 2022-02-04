
def parseForm(browser,current_url):
    browser.open(current_url)
    print('************************************************')
    print('PAGE :'+str(current_url))
    forms=browser.page.find_all('form')
    for form in forms:
        print('FORM INPUTS:')
        print('******************')
        print('* Name * Value  ')
        print('******************')
        inputs = form.find_all('input')
        for input in inputs:
            name = '' if input.has_attr('name') is False else input['name']
            value = '' if input.has_attr('value') is False else input['value']
            print('* ' + name + ' * ' + value + '' + '   ')