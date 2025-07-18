# AI Clinical Consistency Checker

**AI-powered tool for flagging inconsistent information across essential clinical trial documents (protocol, ICF, IB, regulatory letters, etc.).**

Extracts and compares core trial parameters using a modular pipeline. Outputs a human-friendly table and a timestamped CSV report.

---

## Features

- **Batch ingestion:** Converts all PDFs and Word docs in `raw_docs/` to plain text in `extracted_txts/`
- **Rule-based extraction:** Finds key clinical trial parameters (protocol number, version, sample size, etc.) in each document
- **Automated consistency check:** Compares all documents, flags mismatches, and prints a side-by-side table
- **CSV report:** Saves every result as a timestamped file in `reports/` for easy sharing and audit

---

## Project Structure
ai-consistency-checker/
├── batch_ingest.py # Converts all docs in raw_docs/ to text in extracted_txts/
├── ingest.py # PDF/DOCX text extraction
├── parameter_extraction.py # Extracts trial parameters from text (modular, AI-ready)
├── consistency_checker.py # Compares docs, prints table, saves CSV
├── requirements.txt # Required Python packages
├── raw_docs/ # Place your PDF/DOCX files here
├── extracted_txts/ # Auto-generated .txt files go here
├── reports/ # CSV reports saved here
└── README.md

---

## Quick Start

1. **Prepare your documents:**

Place your clinical trial documents (`.pdf` or `.docx`) in the `raw_docs/` folder.

2. **Convert to text:**

python batch_ingest.py

All extracted .txt files will appear in extracted_txts/

3. **Run the consistency checker:**

python consistency_checker.py

The table is printed in your terminal.

A timestamped CSV report appears in reports/

4. Open the CSV report in Excel, Google Sheets, etc.

Requirements
Python 3.8 or higher

Install dependencies with:
pip install -r requirements.txt

To Do / Roadmap
Add LLM/AI-powered parameter extraction for higher accuracy

Enhance reporting (HTML, Excel, etc.)

Integration as a plugin, API, or web dashboard

License
GLP-3 License

Created by DarkStealthGothic
Inspired by real-world challenges in clinical trial operations and compliance.
