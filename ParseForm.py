def parseForm(browser, all_links):
    form_list = {}  # key=URL: value=forms
    for link in all_links:
        browser.open(link)
        forms = browser.page.find_all('form')

        form_list[link] = forms
        for form in forms:
            print('************************************************')
            print('PAGE :' + str(link))
            print('FORM INPUTS:')
            print('******************')
            print('* Name * Value  ')
            print('******************')
            inputs = form.find_all('input')
            for input in inputs:
                name = '' if input.has_attr('name') is False else input['name']
                value = '' if input.has_attr('value') is False else input['value']
                print('* ' + name + ' * ' + value + '' + '   ')
    return form_list
