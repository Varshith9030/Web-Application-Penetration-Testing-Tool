from reportlab.pdfgen import canvas

def generate_report(vulnerabilities):
    pdf = canvas.Canvas("vulnerability_report.pdf")
    pdf.drawString(100, 800, "Vulnerability Report")
    y = 750
    for vuln in vulnerabilities:
        pdf.drawString(50, y, vuln)
        y -= 20
    pdf.save()

# Test
generate_report(["SQL Injection on Login Page", "XSS on Search Page"])
