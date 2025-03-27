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
Here’s how you can describe how you solved the issue:  

---

I encountered an issue where Google displayed the error: *"Couldn’t sign you in. This browser or app may not be secure."* when attempting to log in using Playwright. To troubleshoot, I researched common automation detection mechanisms used by Google. I identified that Chrome flags like `--enable-automation` and `Blink features` settings were likely causing Google to block the login attempt.  

To resolve this, I modified the browser launch options by adding:  

```python
options = {
    'args': ["--disable-blink-features=AutomationControlled"],
    'ignore_default_args': ["--enable-automation"],
    "headless": False
}
```  

These options help bypass automation detection by disabling Blink's `AutomationControlled` feature and removing the `--enable-automation` argument. After applying these changes, Playwright was able to proceed with the login process without triggering the security warning.
