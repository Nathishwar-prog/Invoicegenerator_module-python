# QuickInVoice - Automated Invoice Generator

**QuickInVoice** is a Python package designed to simplify invoice generation for businesses and freelancers. It provides an easy-to-use interface to create, manage, and export invoices in PDF format.

[![PyPI](https://img.shields.io/pypi/v/quickinvoice.svg)](https://pypi.org/project/quickinvoice/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/quickinvoice.svg)](https://pypi.org/project/quickinvoice/)
[![Downloads](https://img.shields.io/pypi/dm/quickinvoice.svg)](https://pypi.org/project/quickinvoice/)

---

## Features 🚀

- **📄 Generate invoices** with itemized details and tax calculations.
- **💰 Automatic tax calculations** based on specified tax rates.
- **🖨️ Export invoices to PDF** with customizable templates.
- **⚙️ Easy integration** into any Python application.
- **✅ Unit-tested and reliable** for production use.

---
## Installation 📥

Install QuickInVoice via pip:


```bash
pip install quick-in-voice

```
## Example script
```` bash
from quick_in_voice import InvoiceGenerator

# Define invoice items
items = [
    {"description": "Web Design", "quantity": 2, "price": 500},
    {"description": "SEO Services", "quantity": 1, "price": 750}
]

# Create and generate invoice
invoice = InvoiceGenerator(
    client_name="TechCorp Solutions", 
    client_address="123 Innovation Street, Tech City, TC 12345",
    items=items,
    tax_rate=0.1  # 10% tax rate
)

# generate the pdf in your preffered name 
invoice.generate_pdf("client_invoice.pdf")

````


