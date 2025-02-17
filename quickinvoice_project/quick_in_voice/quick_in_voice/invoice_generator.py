from fpdf import FPDF
import datetime

class InvoiceGenerator:
    def __init__(self, client_name, client_address, items, tax_rate=0.1):
        self.client_name = client_name
        self.client_address = client_address
        self.items = items
        self.tax_rate = tax_rate
        self.total = 0

    def calculate_total(self):
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        tax = subtotal * self.tax_rate
        self.total = subtotal + tax
        return self.total

    def generate_pdf(self, filename="invoice.pdf"):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, f"Invoice for {self.client_name}", ln=True, align="C")
        pdf.cell(200, 10, f"Address: {self.client_address}", ln=True, align="L")

        pdf.cell(200, 10, "", ln=True)  # Spacer

        pdf.cell(80, 10, "Description", 1)
        pdf.cell(40, 10, "Quantity", 1)
        pdf.cell(40, 10, "Price", 1, ln=True)

        for item in self.items:
            pdf.cell(80, 10, item['description'], 1)
            pdf.cell(40, 10, str(item['quantity']), 1)
            pdf.cell(40, 10, f"${item['price']:.2f}", 1, ln=True)

        pdf.cell(200, 10, "", ln=True)  # Spacer
        pdf.cell(80, 10, "Total:", 1)
        pdf.cell(80, 10, f"${self.calculate_total():.2f}", 1, ln=True)

        pdf.output(filename)
        print(f"Invoice saved as {filename}")

# Example usage
if __name__ == "__main__":
    items = [
        {"description": "Website Development", "quantity": 1, "price": 1000},
        {"description": "SEO Optimization", "quantity": 1, "price": 500}
    ]
    invoice = InvoiceGenerator("XYZ Corp", "456 Business Rd", items)
    invoice.generate_pdf("my_invoice.pdf")
