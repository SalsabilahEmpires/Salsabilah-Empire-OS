"""
Billing Module for SR Electronics Park - Salsabilah-Empire-OS.
Developed by: MD. AL AMIN SOHAG
Features: Auto-generated Invoice, Timestamp, and File Logging.
"""

import datetime
import uuid

def create_professional_bill(customer, product, price, discount=0):
    """
    Calculates the final bill, records details, and logs to a file.
    """
    vat_rate = 0.05
    total_vat = price * vat_rate
    final_price = (price + total_vat) - discount
    
    # ইনভয়েস জেনারেশন
    invoice_no = str(uuid.uuid4())[:8].upper()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    bill_content = f"""
--- SR ELECTRONICS PARK ---
Invoice No: {invoice_no}
Date: {timestamp}
Customer: {customer}
Product: {product}
Base Price: {price:.2f} BDT
VAT (5%): {total_vat:.2f} BDT
Discount: {discount:.2f} BDT
---------------------------
Net Total: {final_price:.2f} BDT
---------------------------
"""
    # কনসোলে আউটপুট দেখানো
    print(bill_content)
    
    # ফাইল লগিং (billing_history.txt এ তথ্য সংরক্ষণ)
    try:
        with open("billing_history.txt", "a", encoding="utf-8") as file:
            file.write(bill_content + "\n")
        print("Success: Invoice saved to billing_history.txt")
    except Exception as e:
        print(f"Error saving log: {e}")
    
    return final_price

# Example Usage
if __name__ == "__main__":
    create_professional_bill("Global Client", "MyOne TV", 32500, 500)
