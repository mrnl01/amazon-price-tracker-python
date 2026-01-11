# Amazon Price Tracker

A Python-based web scraping project that tracks prices of products on Amazon. 
Built using **BeautifulSoup** and **Requests**, this project automatically checks the current price of a product and can send an email alert when the price drops below a set threshold.

## Features
- Scrapes product details like **title** and **price** from Amazon.
- Converts the price string to a numeric value for comparison.
- Sends an **email alert** if the price falls below a user-defined threshold.
- Saves the HTML content locally for reference or debugging.

## Technologies Used
- Python 3.13
- BeautifulSoup4
- Requests
- smtplib (for sending email)
- dotenv (for managing environment variables)

**Create a .env file with your email credentials:**
USER_EMAIL=your_email@example.com
YOUR_PASSWORD=your_app_password
SMTP_ADDRESS=smtp.example.com
