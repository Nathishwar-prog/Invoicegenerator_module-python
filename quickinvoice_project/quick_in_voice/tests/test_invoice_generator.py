import sys
import os

# Add the parent directory to Python path to find the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quick_in_voice.invoice_generator import InvoiceGenerator

def test_calculate_total():
    items = [
        {"description": "Service A", "quantity": 2, "price": 100},
        {"description": "Service B", "quantity": 1, "price": 200}
    ]
    invoice = InvoiceGenerator("Test Corp", "123 Test St", items, tax_rate=0.1)
    assert invoice.calculate_total() == 440.0  # Corrected expected value

