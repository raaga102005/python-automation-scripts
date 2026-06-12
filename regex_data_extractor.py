import re
import pandas as pd

def extract_emails(text):
    """
    Extracts all email addresses from any block of text.
    
    Real use case: client sends you a 50-page document
    and needs all email addresses extracted into Excel.
    Doing this manually = hours. This script = seconds.
    """
    pattern = r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    # Remove duplicates while preserving order
    seen = set()
    unique_emails = []
    for email in emails:
        email_lower = email.lower()
        if email_lower not in seen:
            seen.add(email_lower)
            unique_emails.append(email_lower)
    return unique_emails


def extract_phone_numbers(text):
    """
    Extracts and standardises Indian phone numbers from text.
    Handles formats: 9876543210, +91-9876543210, (080) 4567-8901
    """
    pattern = r'[\+\(]?[\d\s\-\(\)]{10,15}'
    raw_phones = re.findall(pattern, text)
    
    clean_phones = []
    for phone in raw_phones:
        digits = re.sub(r'\D', '', phone)
        if len(digits) == 10:
            clean_phones.append(digits)
        elif len(digits) == 12 and digits.startswith('91'):
            clean_phones.append(digits[2:])
    
    return list(set(clean_phones))


def extract_prices(text):
    """
    Extracts prices in INR and USD from text.
    Handles: ₹45,000 | $599.99 | Rs.1200
    """
    pattern = r'(?:₹|Rs\.?|\$)\s?[\d,]+(?:\.\d{2})?'
    prices = re.findall(pattern, text)
    
    result = []
    for price in prices:
        currency = 'INR' if '₹' in price or 'Rs' in price else 'USD'
        amount = float(re.sub(r'[^\d.]', '', price.replace(',', '')))
        result.append({'Currency': currency, 'Amount': amount, 'Original': price.strip()})
    
    return result


def clean_dataframe_column(df, column, pattern, replacement=''):
    """
    Applies regex cleaning to an entire DataFrame column.
    
    Example: remove all special characters from a phone column
    clean_dataframe_column(df, 'Phone', r'[^\d]', '')
    """
    df[column] = df[column].astype(str).apply(
        lambda x: re.sub(pattern, replacement, x).strip()
    )
    return df


def extract_from_file(filepath):
    """
    Master function: reads any text file and extracts
    all emails, phones, and prices into a structured Excel report.
    
    This is a real deliverable for data extraction gigs.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"Processing file: {filepath}")
    print(f"File size: {len(text)} characters\n")
    
    emails = extract_emails(text)
    phones = extract_phone_numbers(text)
    prices = extract_prices(text)
    
    print(f"Found {len(emails)} unique emails")
    print(f"Found {len(phones)} phone numbers")
    print(f"Found {len(prices)} prices")
    
    # Save to Excel with separate sheets
    with pd.ExcelWriter('extracted_data.xlsx') as writer:
        pd.DataFrame({'Email': emails}).to_excel(
            writer, sheet_name='Emails', index=False
        )
        pd.DataFrame({'Phone': phones}).to_excel(
            writer, sheet_name='Phones', index=False
        )
        pd.DataFrame(prices).to_excel(
            writer, sheet_name='Prices', index=False
        )
    
    print("\nSaved to extracted_data.xlsx")
    return emails, phones, prices


if __name__ == "__main__":
    # Test with sample text
    sample = """
    Our sales team can be reached at sales@company.com 
    or support@helpdesk.org. Call us at 9876543210 
    or +91-8765432109. Our premium plan costs ₹45,000 
    per year or $599.99 for international customers.
    For enterprise pricing contact enterprise@company.com
    or call 07654321098. Basic plan starts at ₹12,000.
    """
    
    print("=== Email Extraction ===")
    print(extract_emails(sample))
    
    print("\n=== Phone Extraction ===")
    print(extract_phone_numbers(sample))
    
    print("\n=== Price Extraction ===")
    for price in extract_prices(sample):
        print(price)
