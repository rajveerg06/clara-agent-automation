# Clara Agent Automation Pipeline

An automation workflow that converts customer call transcripts into versioned AI voice agent configurations.

## Overview

This project simulates Clara's internal setup process for service businesses (for example, fire protection, sprinkler, and electrical providers).

The pipeline:

1. Processes **demo call transcripts** to generate an initial agent configuration (**v1**).
2. Processes **onboarding transcripts** to apply confirmed updates and generate **v2**.
3. Produces a **changelog** so every configuration update is traceable.

The result is a repeatable, transparent, and zero-cost configuration workflow.

## Architecture

### v1 Flow (Demo)

```text
Demo Call Transcript
  -> Extract Business Rules
  -> Generate account_memo.json
  -> Generate agent_spec.json
  -> Store Configuration (v1)
```

### v2 Flow (Onboarding)

```text
Onboarding Transcript
  -> Extract Updates
  -> Update account_memo.json
  -> Generate updated agent_spec.json
  -> Store Configuration (v2)
  -> Generate changelog
```

## Features

- Automated extraction of service business rules from transcripts
- Structured `account_memo.json` generation
- AI voice agent draft spec generation (`agent_spec.json`)
- Versioned outputs (`v1` -> `v2`)
- Explicit change tracking through account-level changelog files
- Reproducible local pipeline
- No paid APIs required

## Project Structure

```text
clara-agent-automation/
  dataset/
    demo_calls/
      demo_call_1.txt
    onboarding_calls/
      onboarding_1.txt
  outputs/
    accounts/
      ACC_xxxxx/
        v1/
          account_memo.json
          agent_spec.json
        v2/
          account_memo.json
          agent_spec.json
  changelog/
    ACC_xxxxx_changes.json
  scripts/
    extract_demo_data.py
    extract_onboarding_updates.py
    generate_account_memo.py
    generate_agent_spec.py
    generate_changelog.py
    update_account_version.py
    run_demo_pipeline.py
    run_onboarding_pipeline.py
    version_manager.py
  workflows/
  README.md
```

## Dataset Expectations

Place transcripts in the following folders:

- `dataset/demo_calls/`
- `dataset/onboarding_calls/`

### Demo Calls

Demo transcripts capture initial discovery conversations and are used to produce the first draft configuration.

### Onboarding Calls

Onboarding transcripts capture confirmed operational details (for example: business hours, emergency routing, and service policies) and are used to update `v1` into `v2`.

## Running The Pipeline

Run commands from the repository root.

### 1. Generate Initial Agent (v1)

```bash
python scripts/run_demo_pipeline.py
```

This step will:

- read demo transcripts
- extract business rules
- generate account memo
- generate agent spec
- write output to `outputs/accounts/<account_id>/v1/`

### 2. Apply Onboarding Updates (v2)

```bash
python scripts/run_onboarding_pipeline.py
```

This step will:

- read onboarding transcripts
- extract updates
- update account memo
- regenerate agent spec
- write output to `outputs/accounts/<account_id>/v2/`
- generate changelog in `changelog/`

## Output Artifacts

For each account, the pipeline generates:

### 1. Account Memo (`account_memo.json`)

Structured operational data extracted from transcripts.

Typical fields include:

- `account_id`
- `company_name`
- `business_hours`
- `services_supported`
- `emergency_definition`
- `routing_rules`
- `questions_or_unknowns`

### 2. Agent Specification (`agent_spec.json`)

Draft voice agent configuration, including:

- agent name
- voice style
- system prompt
- version metadata

### 3. Changelog (`ACC_<id>_changes.json`)

Diff-style record of changes between `v1` and `v2`.

```json
{
  "business_hours": {
    "old": null,
    "new": {
      "days": "Mon-Fri",
      "start": "08:00",
      "end": "18:00"
    }
  }
}
```

## Design Decisions

### Modular Scripts

Each workflow stage is a separate script, which keeps the pipeline easy to maintain and test.

### Versioned Output Model

Configuration snapshots are stored by version:

- `v1`: generated from demo calls
- `v2`: updated with onboarding details

### Transparent Change Tracking

Differences between versions are stored in changelog files for easy audit and review.

### Zero-Cost Constraint

The implementation uses local Python scripts, rule-based extraction, and file storage only (no paid services).

## Future Improvements

- Integrate with `n8n` for workflow orchestration
- Add local Whisper-based transcription
- Build a dashboard to monitor generated agents
- Integrate with Retell API for direct agent creation
- Improve extraction accuracy with stronger NLP logic

## Demo Walkthrough

1. Run `python scripts/run_demo_pipeline.py`.
2. Inspect generated `v1` files in `outputs/accounts/<account_id>/v1/`.
3. Run `python scripts/run_onboarding_pipeline.py`.
4. Inspect updated `v2` files and changelog output.
