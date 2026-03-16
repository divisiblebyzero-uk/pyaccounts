# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**PyAccounts** is a Python-based accounting system that processes Chart of Accounts (CoA) and transactions to generate financial reports. The system ingests account hierarchies and transactions from CSV files, infers missing account mappings, and produces financial statements like P&L reports.

## Core Functional Areas

### 1. Chart of Accounts (CoA) Management
- Ingest account data from CSV files (see REQUIREMENTS.md for schema)
- Categorize accounts into high-level types: EQUITY, ASSET, BANK, LIABILITY, CREDIT, INCOME, EXPENSE
- Build nested hierarchical structure representing CoA paths (e.g., `Assets/CurrentAssets/CurrentAccountSole`)

### 2. Transaction Processing & Journals
- Ingest transactions from CSV files with Date, Description, Amount
- Infer missing account mappings (debit/credit accounts) based on:
  - Known account context provided during upload
  - Transaction description matching patterns
- Store processed transactions as Journal entries

### 3. Financial Reporting
- Generate Profit & Loss statements:
  - Monthly breakdowns for a given year
  - Sum INCOME and EXPENSE account totals
  - Calculate and display Profit/Loss

## Key Data Files

See REQUIREMENTS.md for detailed file format specifications:
- **accounts.csv**: Chart of Accounts with Type, CoA Path, Account Name, Code, Description, Currency, Placeholder
- **transactions.csv**: Transactions with Date, Description, Amount

## Development Setup & Commands

> Project is in early stages. Update this section as development progresses.

- **Create virtual environment**: `python -m venv venv` (or `python3` on Linux/Mac)
- **Activate venv**: `source venv/Scripts/activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
- **Install dependencies**: `pip install -e .` (once pyproject.toml or setup.py is created)
- **Run tests**: `pytest` (add `-v` for verbose output)
- **Run single test**: `pytest tests/test_module.py::test_function_name`

## Architecture Notes

> To be populated as architecture solidifies. Key areas to document:
> - How CoA hierarchies are represented in memory
> - Account matching/inference algorithm
> - Journal entry structure
> - Report generation pipeline
