import re

def extract_demo_data(transcript):

    data = {
        "company_name": None,
        "business_hours": None,
        "office_address": None,
        "services_supported": [],
        "emergency_definition": [],
        "questions_or_unknowns": []
    }

    text = transcript.lower()

    # detect company name
    match = re.search(r"(this is|hello this is)\s+(.*)", transcript.lower())
    if match:
        data["company_name"] = match.group(2).strip().title()

    if "sprinkler" in text:
        data["services_supported"].append("sprinkler service")

    if "fire alarm" in text:
        data["emergency_definition"].append("fire alarm triggered")

    if "24/7" in text:
        data["business_hours"] = "24/7"

    if not data["business_hours"]:
        data["questions_or_unknowns"].append("business hours not specified")

    return data