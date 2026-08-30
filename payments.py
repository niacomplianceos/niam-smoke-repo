"""Checkout and billing. Fixture file for scanner testing."""

import stripe


def charge_customer(email, full_name, address, card_number, amount_inr):
    customer = stripe.Customer.create(
        email=email,
        name=full_name,
        address=address,
    )

    charge = stripe.PaymentIntent.create(
        customer=customer.id,
        amount=amount_inr,
        currency="inr",
        payment_method_data={"card": {"number": card_number}},
    )

    cursor.execute(
        "INSERT INTO billing_events (customer_email, amount, card_last4) VALUES (%s, %s, %s)",
        (email, amount_inr, card_number[-4:]),
    )
    return charge.id


def refund(charge_id, reason):
    return stripe.Refund.create(payment_intent=charge_id, reason=reason)
