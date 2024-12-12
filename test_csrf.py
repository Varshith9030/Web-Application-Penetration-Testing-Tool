def test_csrf(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    for form in forms:
        if not form.find('input', {'name': 'csrf_token'}):
            print("CSRF vulnerability detected!")

# Test
test_csrf("http://localhost/dvwa/")
