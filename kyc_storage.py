"""KYC document handling. Fixture file for scanner testing."""

import boto3

s3 = boto3.client("s3")


def upload_identity_document(user_id, aadhaar_number, pan_number, passport_scan_bytes):
    """Uploads government ID scans to object storage."""
    key = f"kyc/{user_id}/passport.jpg"
    s3.put_object(Bucket="niam-smoke-kyc", Key=key, Body=passport_scan_bytes)

    cursor.execute(
        "INSERT INTO kyc_records (user_id, aadhaar, pan_number, doc_key) VALUES (%s, %s, %s, %s)",
        (user_id, aadhaar_number, pan_number, key),
    )
    return key


def record_last_known_location(user_id, latitude, longitude, ip_address):
    cursor.execute(
        "INSERT INTO user_location (user_id, lat, lng, ip_address) VALUES (%s, %s, %s, %s)",
        (user_id, latitude, longitude, ip_address),
    )
