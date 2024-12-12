from bs4 import BeautifulSoup
import requests

def extract_inputs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    inputs = []
    for form in forms:
        for input_tag in form.find_all('input'):
            inputs.append(input_tag.get('name'))
    return inputs
