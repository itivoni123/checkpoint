# Gmail Login

## Overview
This project implements a **Page Object Model (POM)** for handling login functionality using **Playwright** with Python. The `LogIn` class provides an abstraction for automating login flows in test cases.

## Features
- Uses **Playwright** for browser automation.
- Implements the **Page Object Model (POM)** pattern.
- Supports **asynchronous testing** with `pytest.mark.asyncio`.
- Returns the browser instance for external management.

## Installation
To install the required dependencies from the `requirements.txt` file, run:
```sh
pip install -r requirements.txt
playwright install
```

## Usage
### Running the Tests
Execute the test using pytest:
```sh
pytest test_gmail_login.py
```
```

