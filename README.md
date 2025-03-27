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
I encountered an issue where Google displayed the error: *"Couldn’t sign you in. This browser or app may not be secure."* when trying to log in using Playwright. To troubleshoot, I searched for solutions on Google and YouTube to understand why this error was occurring.  

Through my research, I found that Google detects automation tools like Playwright by checking certain browser flags, such as `--enable-automation` and Blink features. Based on the solutions I found, I modified the browser launch options to bypass automation detection:  

```python
options = {
    'args': ["--disable-blink-features=AutomationControlled"],
    'ignore_default_args': ["--enable-automation"],
    "headless": False
}
```  

By disabling Blink’s `AutomationControlled` feature and removing the `--enable-automation` argument, I was able to successfully log in without triggering the security warning.
