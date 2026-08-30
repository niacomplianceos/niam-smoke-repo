"""Transactional messaging. Fixture file for scanner testing."""

import requests


def send_order_sms(phone, message_body):
    """Twilio — outbound SMS."""
    return requests.post(
        "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Messages.json",
        data={"To": phone, "From": "+150055501000", "Body": message_body},
    )


def send_receipt_email(email, full_name, order_summary):
    """SendGrid — outbound email."""
    return requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        json={
            "personalizations": [{"to": [{"email": email, "name": full_name}]}],
            "content": [{"type": "text/plain", "value": order_summary}],
        },
    )


def log_notification(user_id, channel, delivered_at):
    cursor.execute(
        "INSERT INTO notification_log (user_id, channel, delivered_at) VALUES (%s, %s, %s)",
        (user_id, channel, delivered_at),
    )
