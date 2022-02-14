def test(browser, form_dict, vectors, sanitized_list, sensitive_list, timeout):
    print("*********************************************************")
    print("Testing with vectors...")
    print("This may take a while with a large vectors file...")
    fail_status_counter = 0;

    for url, form_list in form_dict.items():
        browser.open(url)
        for form in form_list:
            for vector in vectors:
                inputs = form.findAll('input')

                for test_input in inputs:
                    if test_input.has_attr('name'):
                        input_type = test_input['name']
                    elif test_input.has_attr('type'):
                        input_type = test_input['type']
                    if input_type == "submit":
                        value = 'submit'
                    else:
                        value = vector

                # run tests
                try:
                    browser.select_form()
                    browser[input_type] = value
                    res = browser.submit_selected()
                    if not check_response_status(res, vector, input_type, value):
                        fail_status_counter += 1;
                except:
                    pass

    # test if it was sanitized (<,>)
    # sensitive data leak
    # Number of possible DOS vulnerabilities: (number of response slower than threadhold: seconds=slow/1000 )
    # Number of HTTP/Response Code Errors(translate to human readable format)
    print("*************************************")
    print("*          TEST RESULTS:            *")
    print("*************************************")
    print("Number of Unsanitized inputs: ")
    print("Number of possible Sensitive Data Leakages: ")
    print("Number of possible DOS vulnerabilities: ")
    print("Number of HTTP/Response Code Errors: " + str(fail_status_counter))
    cookies = browser.get_cookiejar()
    for c in cookies:
        print(c.name + '=>' + c.value)


def check_response_status(res, vector, input_type, value):
    is_ok = True
    status_code = res.status_code
    if status_code != 200:
        is_ok = False
        print('-----------------ERROR-----------------')
        print(str(status_code) + "=>\n"),
        print('input type=>' + str(input_type) + '| value=>' + str(value))
        print("Error loading " + res.url + " with params " + str(vector))
    return is_ok


def check_sanitized(res):
    pass


def check_sensitive(res):
    pass
