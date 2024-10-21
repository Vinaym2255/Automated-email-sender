from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

app = Flask(__name__)

# Load email configuration from environment variables
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    email_data = request.json
    required_fields = ['email', 'name', 'invoice_no', 'amount', 'due_date', 'reminder_date', 'has_paid']

    # Check for missing fields
    for data in email_data:
        missing_fields = [field for field in required_fields if field not in data or not data[field]]
        if missing_fields:
            return jsonify({"message": f"The following field(s) are not filled: {', '.join(missing_fields)}"}), 400

    try:
        # Get today's date for comparison
        today = datetime.today().date()

        for data in email_data:
            # Convert the reminder date from string to date
            reminder_date = datetime.strptime(data['reminder_date'], '%Y-%m-%d').date()
            
            # Check if the user has not paid and the reminder date is today or has passed
            if data['has_paid'] == "No" and reminder_date <= today:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = data['email']
                msg['Subject'] = f"Invoice No: {data['invoice_no']}"

                body = f"""
                <p>Hi {data['name']},</p>

                <p>We hope you are well.</p>

                <p>This is a reminder that an amount of <strong>Rs {data['amount']}</strong> is due in respect of our invoice <strong>{data['invoice_no']}</strong>.</p>
                <p>The due date for the payment is <strong>{data['due_date']}</strong>.</p>

                <p>Kindly make the payment at your earliest convenience.</p>

                <p>Thank you!</p>
                """

                msg.attach(MIMEText(body, 'html'))

                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    server.send_message(msg)

        return jsonify({"message": "Emails sent successfully!"})

    except Exception as e:
        return jsonify({"message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
