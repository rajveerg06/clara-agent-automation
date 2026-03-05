Clara Agent Automation Pipeline
Overview

This project implements an automation pipeline that converts customer call transcripts into AI voice agent configurations.

The system processes demo call transcripts to generate an initial agent configuration (v1) and later processes onboarding transcripts to update the agent configuration (v2) while tracking all changes.

This simulates the internal workflow used to configure Clara AI voice agents for service-based businesses such as fire protection companies, sprinkler contractors, and electrical service providers.

The pipeline ensures that configuration changes are versioned, traceable, and reproducible.

Architecture

Demo Call Transcript
↓
Extract Business Rules
↓
Generate Account Memo JSON
↓
Generate Agent Specification
↓
Store Agent Configuration (v1)

Onboarding Transcript
↓
Extract Updates
↓
Apply Updates to Account Memo
↓
Generate Updated Agent Specification
↓
Store Updated Configuration (v2)
↓
Generate Change Log

Features

Automated extraction of service business rules from transcripts

Structured Account Memo JSON generation

AI voice agent draft specification generation

Version control for agent configurations (v1 → v2)

Change tracking using a changelog

Reproducible automation pipeline

Zero-cost implementation (no paid APIs)

Project Structure
clara-agent-automation
│
├── dataset
│   ├── demo_calls
│   │   └── demo_call_1.txt
│   │
│   └── onboarding_calls
│       └── onboarding_1.txt
│
├── outputs
│   └── accounts
│       └── ACC_xxxxx
│           ├── v1
│           │   ├── account_memo.json
│           │   └── agent_spec.json
│           │
│           └── v2
│               ├── account_memo.json
│               └── agent_spec.json
│
├── changelog
│   └── ACC_xxxxx_changes.json
│
├── scripts
│   ├── extract_demo_data.py
│   ├── extract_onboarding_updates.py
│   ├── generate_account_memo.py
│   ├── generate_agent_spec.py
│   ├── generate_changelog.py
│   ├── update_account_version.py
│   ├── run_demo_pipeline.py
│   ├── run_onboarding_pipeline.py
│   └── version_manager.py
│
├── workflows
│
└── README.md

Dataset
The pipeline expects transcripts to be placed in the following directories:
dataset/demo_calls/
dataset/onboarding_calls/

Demo Calls

Demo call transcripts contain initial conversations with potential clients.
These transcripts are used to extract preliminary configuration details.

Onboarding Calls

Onboarding transcripts contain confirmed operational details such as:

business hours

emergency routing rules

service handling policies

These transcripts update the agent configuration from v1 to v2.

Running the Pipeline
Step 1 — Generate Initial Agent (v1)

Run the demo pipeline:

python scripts/run_demo_pipeline.py

This will:

read demo transcripts

extract business rules

generate account memo

create agent specification

store v1 configuration

Outputs are stored in:

outputs/accounts/<account_id>/v1/
Step 2 — Apply Onboarding Updates (v2)

Run the onboarding pipeline:

python scripts/run_onboarding_pipeline.py

This will:

read onboarding transcripts

extract updates

modify the account memo

generate updated agent specification

create v2 configuration

generate changelog

Outputs are stored in:

outputs/accounts/<account_id>/v2/
Output Artifacts

For each account the system generates:

Account Memo JSON

Contains structured operational information extracted from transcripts.

Example fields:

account_id

company_name

business_hours

services_supported

emergency_definition

routing rules

questions_or_unknowns

Agent Draft Specification

Represents the configuration required to create a Retell voice agent.

Includes:

agent name

voice style

system prompt

version information

Changelog

Tracks differences between v1 and v2 configurations.

Example:

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
Design Decisions
Modular Pipeline

Each stage of the workflow is implemented as a separate script to ensure modularity and maintainability.

Versioned Configuration

Agent configurations are stored in versioned directories:

v1 → demo call configuration  
v2 → onboarding update configuration
Change Tracking

Changes between versions are captured in a changelog to maintain transparency in configuration updates.

Zero-Cost Constraint

The system uses:

Python

Local file storage

Rule-based extraction

This satisfies the assignment requirement of no paid APIs or services.

Future Improvements

Possible enhancements for production deployment include:

Integration with n8n workflow automation

Local Whisper-based speech-to-text transcription

Web dashboard for monitoring generated agents

Integration with Retell API for automatic agent creation

Improved NLP-based extraction for higher accuracy

Demo

The system can be demonstrated by:

Running the demo pipeline

Inspecting generated v1 outputs

Running the onboarding pipeline

Inspecting v2 outputs and changelog
