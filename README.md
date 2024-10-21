# Automated Email Sender

## Project Overview

The **Automated Email Sender** is a Python-based application built using Flask. It automates the process of sending bulk emails with customizable details such as recipient name, invoice number, due date, and payment status. The tool is ideal for sending personalized emails to multiple recipients in one go, which makes it useful for managing communication in businesses, billing departments, or customer support.

## Key Features

- **Bulk Email Sending**: Automatically send personalized emails to a large number of recipients.
- **Customizable Recipient Data**: Input custom fields such as name, invoice number, amount due, and payment status.
- **Flexible Input Options**: Easily add or delete rows to manage recipient data, and update fields dynamically.
- **Payment Status Update**: Track and update payment statuses using a "Yes" or "No" dropdown.
- **Simple UI**: A user-friendly interface to manage recipient information and email content.
- **Error Handling**: Feedback provided for both successfully sent emails and errors encountered during the process.

## Project Structure

- `app.py`: The main Flask application file that handles routing and backend logic.
- `templates/index.html`: The front-end interface for inputting recipient data and sending emails.
- `.gitignore`: Ensures sensitive files like environment configurations are not tracked in version control.

## How It Works

1. **Add Recipients**: Enter the recipient details in a form that includes columns for the recipient’s email, name, invoice number, amount due, due date, reminder date, and payment status.
2. **Customize Emails**: Modify the email subject and body according to your needs.
3. **Send Emails**: On submission, the app sends all emails in bulk with the specified details.
4. **Receive Feedback**: After sending, the app provides a summary indicating the status of each email sent (success or error).

## Technologies Used

- **Python (Flask)**: Backend framework for the web application.
- **HTML/CSS**: Frontend interface for user input.
- **SMTP**: Email protocol used for sending emails.
- **SQLite**: (If applicable, for storing recipient data and email logs).

## Installation & Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Vinaym2255/Automated-email-sender.git
   cd Automated-email-sender
