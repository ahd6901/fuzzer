def test(browser, form_dict, vectors, sanitized_list, sensitive_list, timeout):
    print("*********************************************************")
    print("Testing with vectors...")
    print("This may take a while with a large vectors file...")
    failed_status_counter = 0;
    dos_counter = 0;
    unsanitized_counter = 0;
    sensitive_counter = 0;

    for url, form_list in form_dict.items():
        print('===========================URL:' + str(url) + " ======================")
        browser.open(url)
        for form in form_list:
            for vector in vectors:
                print("====Testing with vector '" + str(vector) + "' ")
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
                    if not check_response_status(res):
                        failed_status_counter += 1;
                    if not check_dos(res, timeout):
                        dos_counter += 1;
                    unsanitized_counter += count_unsanitized(res, sanitized_list, vector)
                    sensitive_counter += count_sensitive(res, sensitive_list)

                except:
                    pass

    print("*************************************")
    print("*          TEST RESULTS:            *")
    print("*************************************")
    print("Number of Unsanitized inputs: " + str(unsanitized_counter))
    print("Number of possible Sensitive Data Leakages: "+ str(sensitive_counter))
    print("Number of possible DOS vulnerabilities: " + str(dos_counter))
    print("Number of HTTP/Response Code Errors: " + str(failed_status_counter))


def check_dos(res, timeout):
    time_taken = round(res.elapsed.total_seconds() * 1000, 2)
    if float(time_taken) > float(timeout):
        print("(Potential DOS Vulnerability) " + res.url + ' tooks ' + str(
            float(time_taken)) + 'ms to load as opposed to ' + str(float(timeout)) + 'ms')
        return False

    return True


def check_response_status(res):
    is_ok = True
    status_code = res.status_code
    if status_code != 200:
        is_ok = False
        print('-----------------ERROR-----------------')
        print(str(status_code) + "=>\n"),

        print(res.reason + " for " + res.url)
    return is_ok


def count_unsanitized(res, sanitized_list, vector):
    counter = 0;
    for char in sanitized_list:
        if char in vector and char in res.text:
            print("Character '" + str(char) + "' was not sanitized from input vector '" + str(vector) + "'")
            counter += 1
    return counter


def count_sensitive(res, sensitive_list):
    sensitive_leak_counter=0
    for s in sensitive_list:
        if s in res.text:
            sensitive_leak_counter+=1
            print("(Potential Sensitive data leak)"+ str(s)+ " was found is response")

    return sensitive_leak_counter
