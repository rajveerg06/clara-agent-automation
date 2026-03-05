import os
import json

from extract_onboarding_updates import extract_onboarding_updates
from update_account_version import update_account
from generate_agent_spec import generate_agent_spec
from generate_changelog import generate_changelog


ONBOARDING_PATH = "dataset/onboarding_calls"
OUTPUT_PATH = "outputs/accounts"


def run_onboarding_pipeline():

    onboarding_files = os.listdir(ONBOARDING_PATH)

    accounts = os.listdir(OUTPUT_PATH)

    if not accounts:
        print("No accounts found. Run demo pipeline first.")
        return

    # For simplicity we update the first account
    account_id = accounts[0]

    v1_path = f"{OUTPUT_PATH}/{account_id}/v1/account_memo.json"

    with open(v1_path, "r") as f:
        v1_memo = json.load(f)

    for file in onboarding_files:

        file_path = os.path.join(ONBOARDING_PATH, file)

        with open(file_path, "r") as f:
            transcript = f.read()

        print(f"\nProcessing onboarding file: {file}")

        updates = extract_onboarding_updates(transcript)

        v2_memo = update_account(
            account_id,
            v1_memo,
            updates,
            generate_agent_spec
        )

        changes = generate_changelog(v1_memo, v2_memo)

        os.makedirs("changelog", exist_ok=True)

        with open(f"changelog/{account_id}_changes.json", "w") as f:
            json.dump(changes, f, indent=2)

        print(f"Updated account {account_id} → v2")


if __name__ == "__main__":
    run_onboarding_pipeline()