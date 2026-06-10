# Python Automation Scripts

A collection of Python automation scripts built for real 
business use cases. Each script solves a specific problem 
that saves hours of manual work.

---

## Scripts

### 1. excel_cleaner.py
Cleans messy Excel and CSV files automatically.

What it does:
- Removes empty and duplicate rows
- Strips extra whitespace from text columns
- Standardizes column names
- Generates a grouped summary report

Tech used: pandas, openpyxl

---

### 2. web_scraper.py
Scrapes product listings from any public website into Excel.

What it does:
- Extracts titles, prices, ratings from any listing page
- Handles pagination automatically
- Saves results to CSV
- Polite scraping with delays between requests

Tech used: requests, BeautifulSoup, pandas

---

### 3. file_renamer.py
Renames hundreds of files in a folder in seconds.

What it does:
- Adds custom prefix to all files
- Adds sequential numbering (001, 002, 003...)
- Adds date to filenames
- Dry run mode to preview changes before applying
- Can target specific file extensions only

Tech used: os, shutil, datetime

---

## How to run

Install dependencies:
pip install pandas openpyxl requests beautifulsoup4

Run any script:
python excel_cleaner.py
python web_scraper.py
python file_renamer.py

---

## About

Built by Raaga Priya Madhan — 2nd year CSE student from 
Bangalore specializing in Python automation.

Available for freelance Python automation work.

LinkedIn: https://www.linkedin.com/in/raaga-priya-madhan-5bb688318
Dev.to: https://dev.to/raagawrites
