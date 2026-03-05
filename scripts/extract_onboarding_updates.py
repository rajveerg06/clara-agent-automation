def extract_onboarding_updates(transcript):

    updates = {}

    text = transcript.lower()

    # detect business hours
    if "8am" in text and "6pm" in text:
        updates["business_hours"] = {
            "days": "Mon-Fri",
            "start": "08:00",
            "end": "18:00"
        }

    # detect emergency routing
    if "dispatch technician" in text:
        updates["emergency_routing_rules"] = {
            "route_to": "dispatch technician"
        }

    # detect non emergency scheduling
    if "next business day" in text:
        updates["non_emergency_routing_rules"] = {
            "schedule": "next business day"
        }

    return updates