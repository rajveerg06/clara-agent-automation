import uuid

def generate_account_memo(extracted):

    account_id = "ACC_" + str(uuid.uuid4())[:8]

    memo = {
        "account_id": account_id,
        "company_name": extracted.get("company_name"),
        "business_hours": extracted.get("business_hours"),
        "office_address": extracted.get("office_address"),
        "services_supported": extracted.get("services_supported"),
        "emergency_definition": extracted.get("emergency_definition"),
        "emergency_routing_rules": {},
        "non_emergency_routing_rules": {},
        "call_transfer_rules": {},
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": extracted.get("questions_or_unknowns"),
        "notes": ""
    }

    return memo