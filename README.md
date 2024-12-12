# Web Application Penetration Testing Tool

This is a Python-based tool designed to help security enthusiasts and developers identify common web application vulnerabilities, including **SQL Injection**, **Cross-Site Scripting (XSS)**, and **Cross-Site Request Forgery (CSRF)**. The tool automates vulnerability scanning and generates detailed reports to help users understand the issues in their web applications.

---

## Features

- **SQL Injection Detection**: Scans input fields and URLs for potential SQL Injection vulnerabilities.
- **XSS Detection**: Identifies Cross-Site Scripting vulnerabilities by injecting payloads and analyzing the response.
- **CSRF Detection**: Checks for CSRF vulnerabilities by analyzing form submissions and missing CSRF tokens.
- **Automated Vulnerability Reporting**: Generates a **PDF report** that summarizes the findings, helping users quickly identify and address security issues.

---

## Script Overview

The **Web Application Penetration Testing Tool** consists of a single Python script that performs the following tasks:

1. **User Input (URL)**: The script takes the URL of the target web application as input.
   
2. **SQL Injection Detection**:
   - The tool scans GET and POST parameters for possible SQL Injection vulnerabilities by injecting common payloads and observing the response.
   
3. **XSS Detection**:
   - It checks input fields for potential XSS vulnerabilities by injecting malicious JavaScript payloads and verifying whether the input is reflected back on the page.

4. **CSRF Detection**:
   - The script detects missing or improper CSRF tokens in form submissions and identifies potential vulnerabilities.

5. **Report Generation**:
   - After completing the scan, the tool generates a **PDF report** that outlines any detected vulnerabilities, along with their potential risk levels.

---

## Prerequisites

Before running this tool, make sure you have the following installed on your system:

- **Python 3.x** (recommended version 3.6+)
- **pip** (Python package manager)

You will also need the following libraries:

- `requests`
- `beautifulsoup4`
- `selenium`
- `reportlab`

These can be installed via `pip` by running:

```bash
pip3 install requests beautifulsoup4 selenium reportlab
```

You may also need **Google Chrome** and **ChromeDriver** installed for Selenium to work.

---

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Varshith9030/Web-Application-Penetration-Testing-Tool.git
   cd Web-Application-Penetration-Testing-Tool
   ```

2. Install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Install **Google Chrome** and **ChromeDriver** for Selenium (if not already installed). Follow the [installation guide](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#chrome).

---

## Usage

1. Once the setup is complete, navigate to the project directory and run the tool with the target URL you want to test:

   ```bash
   python3 vulnerability_scanner.py
   ```

2. Enter the URL of the web application you want to test (e.g., `http://localhost/` or any other target URL).

3. The tool will begin scanning for **SQL Injection**, **XSS**, and **CSRF** vulnerabilities.

4. After scanning, the tool will generate a PDF report, `vulnerability_report.pdf`, summarizing all detected issues.

---

## Example

Running the tool:

```bash
python3 vulnerability_scanner.py
```

Sample output:

```
Scanning target: http://localhost/
Detecting SQL Injection...
XSS vulnerabilities found: 2
CSRF vulnerabilities found: 1
PDF report generated: vulnerability_report.pdf
```

---

## Contributing

Feel free to fork the repository, make improvements, and open pull requests. Contributions are welcome!

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- The tool leverages `requests`, `beautifulsoup4`, and `selenium` libraries to perform web scraping and vulnerability scanning.
- **OWASP** for providing vulnerability references.
- **Google Chrome** and **ChromeDriver** for automation via Selenium.

---

## Contact

Developed by **Varshith**  
[LinkedIn Profile](https://www.linkedin.com/in/varshithbonagiri)
