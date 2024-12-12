import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from reportlab.pdfgen import canvas

vulnerabilities = []

def extract_inputs(url):
    print(f"Scanning {url} for input fields...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    inputs = []
    forms = soup.find_all('form')
    for form in forms:
        form_action = form.get('action', url)
        form_method = form.get('method', 'get').lower()
        input_fields = [input_tag.get('name') for input_tag in form.find_all('input')]
        inputs.append({'action': form_action, 'method': form_method, 'fields': input_fields})
    return inputs

def test_sql_injection(url, inputs):
    print("Testing for SQL Injection...")
    payloads = ["' OR '1'='1", "' UNION SELECT NULL --"]
    for form in inputs:
        for field in form['fields']:
            for payload in payloads:
                data = {field: payload}
                if form['method'] == 'post':
                    response = requests.post(url, data=data)
                else:
                    response = requests.get(url, params=data)
                if "error" in response.text.lower() or "sql" in response.text.lower():
                    vulnerabilities.append(f"SQL Injection detected on parameter: {field} with payload: {payload}")
                    print(f"SQL Injection detected on parameter: {field}")
                    break

def test_xss(url):
    print("Testing for XSS...")
    driver = webdriver.Chrome()
    driver.get(url)
    script = "<script>alert('XSS')</script>"
    inputs = driver.find_elements("tag name", 'input')
    for input_field in inputs:
        try:
            input_field.send_keys(script)
            input_field.submit()
        except:
            pass
    try:
        alert = driver.switch_to.alert
        vulnerabilities.append("XSS vulnerability detected!")
        print("XSS vulnerability detected!")
        alert.accept()
    except:
        print("No XSS detected.")
    driver.quit()

def test_csrf(url):
    print("Testing for CSRF...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    for form in forms:
        if not form.find('input', {'name': 'csrf_token'}):
            vulnerabilities.append("CSRF vulnerability detected!")
            print("CSRF vulnerability detected!")

def generate_report(vulnerabilities):
    print("Generating report...")
    pdf = canvas.Canvas("vulnerability_report.pdf")
    pdf.drawString(100, 800, "Vulnerability Report")
    y = 750
    for vuln in vulnerabilities:
        pdf.drawString(50, y, vuln)
        y -= 20
    pdf.save()
    print("Report saved as 'vulnerability_report.pdf'.")

def main():
    target_url = input("Enter the URL to scan: ")
    print("Starting vulnerability scan...")
    inputs = extract_inputs(target_url)
    test_sql_injection(target_url, inputs)
    test_xss(target_url)
    test_csrf(target_url)
    if vulnerabilities:
        generate_report(vulnerabilities)
    else:
        print("No vulnerabilities detected.")

if __name__ == "__main__":
    main()
