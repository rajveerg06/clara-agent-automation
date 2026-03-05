# Clara Agent Automation Pipeline

## Overview

This project builds an automation workflow that converts demo and onboarding call transcripts into AI voice agent configurations.

The system generates a **v1 agent configuration from demo calls** and updates it to **v2 using onboarding calls**, while tracking all configuration changes.

---

## Architecture

Demo Call Transcript  
↓  
Extract Business Rules  
↓  
Account Memo JSON  
↓  
Generate Agent Spec (v1)

Onboarding Transcript  
↓  
Extract Updates  
↓  
Apply Patch to Memo  
↓  
Generate Agent Spec (v2)  
↓  
Generate Changelog

---

## Features

- Automated extraction of service business rules
- Structured account memo generation
- Retell agent configuration generation
- Version control for agent configurations
- Changelog generation for onboarding updates

---

## Project Structure

dataset/  
&nbsp;&nbsp;demo_calls/  
&nbsp;&nbsp;onboarding_calls/

outputs/  
&nbsp;&nbsp;accounts/  
&nbsp;&nbsp;&nbsp;&nbsp;ACC_xxxxx/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v1/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v2/

scripts/

changelog/

---

## Running the System

Run demo pipeline:
python scripts/run_demo_pipeline.py

Run onboarding pipeline:

python scripts/run_onboarding_pipeline.py

---

## Outputs

For each account the system generates:

- Account memo JSON
- Agent draft specification
- Versioned configurations (v1 → v2)
- Changelog describing updates

Step 4

Save it:
CTRL + S
