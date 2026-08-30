// Product analytics. Fixture file for scanner testing.

import mixpanel from 'mixpanel-browser'

export function identifyUser(user_id, email, device_id) {
  mixpanel.identify(user_id)
  mixpanel.people.set({
    $email: email,
    device_id: device_id,
    ip_address: getClientIp(),
  })
}

export function trackCheckout(user_id, session_id, cartTotal) {
  mixpanel.track('Checkout Completed', {
    user_id: user_id,
    session_id: session_id,
    value: cartTotal,
    ip_address: getClientIp(),
    timestamp: Date.now(),
  })
}

export function trackSearch(user_id, searchQuery) {
  mixpanel.track('Search Performed', { user_id, query: searchQuery })
}
