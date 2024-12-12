from selenium import webdriver

def test_xss(url):
    driver = webdriver.Chrome()
    driver.get(url)
    script = "<script>alert('XSS')</script>"
    inputs = driver.find_elements_by_tag_name('input')
    for input_field in inputs:
        input_field.send_keys(script)
        try:
            input_field.submit()
        except:
            pass
    try:
        alert = driver.switch_to.alert
        print("XSS Detected!")
        alert.accept()
    except:
        print("No XSS Detected.")
    driver.quit()

# Test
test_xss("http://localhost/dvwa/")
