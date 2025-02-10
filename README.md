# Data Processing Toolkit
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

A collection of utilities for working with different data formats.

## Features

- **Grade Analyzer**: Calculate student/class averages from CSV
- **JSON Explorer**: Search nested JSON structures and analyze todo lists
- **File Navigator**: Directory inspection utilities

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
# Analyze grades
python -m src.cli analyze-grades data/sample_grades.csv

# Explore JSON
python -m src.cli count-measurements data/weather.json "KUITUVASTE_SUURI_1"
```