# Billing & Invoice Module
# Powered by DeepSeek-V3 Logic

def generate_invoice(customer_name, service, amount):
    invoice_id = f"SAE-{customer_name[:3].upper()}-2026"
    print(f"Creating Invoice {invoice_id} for {customer_name}...")
    print(f"Service: {service} | Amount: {amount} BDT")
    return "✅ Invoice Sent Successfully!"

generate_invoice("Broadband User 01", "5Mbps Internet", 500)
generate_invoice("SR Electronics Dealer", "Inventory Management", 5000)
