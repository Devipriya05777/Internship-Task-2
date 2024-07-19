class Invoice:
    def __init__(self, invoice_number, date, customer_name, items):
        self.invoice_number = invoice_number
        self.date = date
        self.customer_name = customer_name
        self.items = items

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def generate_invoice(self):
        invoice_text = f"Invoice Number: {self.invoice_number}\n"
        invoice_text += f"Date: {self.date}\n"
        invoice_text += f"Customer Name: {self.customer_name}\n\n"
        invoice_text += "Items:\n"
        for item in self.items:
            invoice_text += f"{item['description']} - {item['quantity']} x ${item['price']:.2f} = ${item['quantity'] * item['price']:.2f}\n"
        invoice_text += "\n"
        invoice_text += f"Total Amount: ${self.calculate_total():.2f}\n"
        return invoice_text

# Example usage
items = [
    {'description': 'Widget', 'quantity': 4, 'price': 10.00},
    {'description': 'Gadget', 'quantity': 2, 'price': 15.00}
]

invoice = Invoice(invoice_number="INV12345", date="2024-07-19", customer_name="John Doe", items=items)
print(invoice.generate_invoice())
