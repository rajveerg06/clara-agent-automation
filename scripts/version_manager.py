import os
import json

def save_version(account_id, version, memo, agent):

    folder = f"outputs/accounts/{account_id}/{version}"

    os.makedirs(folder, exist_ok=True)

    with open(f"{folder}/account_memo.json", "w") as f:
        json.dump(memo, f, indent=2)

    with open(f"{folder}/agent_spec.json", "w") as f:
        json.dump(agent, f, indent=2)