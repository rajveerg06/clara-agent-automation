import os
import json

from extract_demo_data import extract_demo_data
from generate_account_memo import generate_account_memo
from generate_agent_spec import generate_agent_spec
from version_manager import save_version


DATASET_PATH = "dataset/demo_calls"


def run_pipeline():

    files = os.listdir(DATASET_PATH)

    for file in files:

        file_path = os.path.join(DATASET_PATH, file)

        with open(file_path, "r", encoding="utf-8") as f:
            transcript = f.read()

        print(f"\nProcessing: {file}")

        # Step 1 — Extract structured data
        extracted = extract_demo_data(transcript)

        # Step 2 — Generate account memo
        memo = generate_account_memo(extracted)

        # Step 3 — Generate agent specification
        agent_spec = generate_agent_spec(memo)

        # Step 4 — Save version v1
        save_version(memo["account_id"], "v1", memo, agent_spec)

        print(f"Created agent for account: {memo['account_id']}")


if __name__ == "__main__":
    run_pipeline()