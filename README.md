# niam-smoke-repo

Throwaway fixtures for verifying the Niam scanner. **Not real code. Not a real product.**
No credentials, no real personal data — every value is a placeholder.

Six files, tuned to trip `diff_parser.DEFAULT_SIGNALS` (the stage-1 keyword pre-filter) so
they reliably reach the Gemini classifier in stage 2.

| File | Data types it should surface | Vendor it should surface |
|---|---|---|
| `signup.py` | email, phone, date_of_birth, consent_or_age | Firebase *(plus a local-DB path with **no** vendor)* |
| `payments.py` | email, address, credit_card, profile_data | Stripe |
| `analytics.js` | user_id, device_id, ip_address, session_token, search_query | Mixpanel |
| `profile_api.ts` | profile_data, address, phone, user_id | *(none — local writes only)* |
| `notifications.py` | phone, email, message_content, user_id | Twilio, SendGrid |
| `kyc_storage.py` | government_id, location, ip_address, user_id | AWS S3 |

## Expected scan result

- **~71 stage-1 candidate lines** (verified against `DEFAULT_SIGNALS`)
- **~12–16 distinct `:DataType` nodes**
- **~5–7 distinct `:Vendor` nodes** — Stripe, Mixpanel, Firebase, Twilio, SendGrid, AWS/S3

That vendor spread is deliberate: six files with three real integrations still produce five to
seven vendor nodes, because `vendor` is free text from the LLM with no taxonomy validation.
**This is the "13 vendors" problem in miniature** — a fast way to confirm the Phase C1 fix
actually splits *detected* from *connected*.

## Expected gaps after reconciliation

`profile_api.ts` writes personal data with **no vendor**, so it should produce
`ungoverned_collection` (low). The vendor-carrying paths should produce `ungoverned_egress`
(high) or `future_obligation` (medium), depending on whether a governing DPDP clause exists and
whether it has commenced. As of August 2026 most of the Act has **not** commenced (Tranche 2 is
13 Nov 2026, Tranche 3 is 13 May 2027), so **expect mostly `future_obligation`.**
That is correct behaviour, not a bug — it is exactly what Phase E6 is about.

## Rules

- Keep this repo **private** and **tiny**.
- Never point a Smoke Check at a repo you care about — Phase A2's `open-pr` tests target this one.
- Regenerate freely. Nothing here is precious.
