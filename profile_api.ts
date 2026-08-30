// Profile management. Fixture file for scanner testing.

interface ProfileUpdate {
  full_name: string
  address: string
  avatar_url: string
  bio: string
  locale: string
}

export async function updateProfile(user_id: string, patch: ProfileUpdate) {
  // Local write only — no third party on this path
  await db.collection('profiles').update({ user_id }, patch)
  return { ok: true }
}

export async function saveDeliveryAddress(user_id: string, address: string, phone: string) {
  await db.collection('addresses').create({ user_id, address, phone })
}

export async function fetchProfile(user_id: string) {
  const res = await fetch(`/internal/profiles/${user_id}`)
  return res.json()
}
