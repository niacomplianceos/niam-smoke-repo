"""Account creation. Fixture file for scanner testing."""

import firebase_admin
from firebase_admin import auth


def create_account(email, phone, date_of_birth, consent, marketing_consent):
    if not consent:
        raise ValueError("consent is required before collecting personal data")

    # Local persistence — no external vendor on this path
    cursor.execute(
        "INSERT INTO users (email, phone, date_of_birth, consent) VALUES (%s, %s, %s, %s)",
        (email, phone, date_of_birth, consent),
    )

    # Identity provider
    user = auth.create_user(email=email, phone_number=phone)
    return user.uid


def verify_age(date_of_birth):
    """Reject minors — DPDP requires parental consent under 18."""
    age = compute_age(date_of_birth)
    if age < 18:
        return {"requires_parental_consent": True, "minor": True}
    return {"requires_parental_consent": False, "minor": False}
