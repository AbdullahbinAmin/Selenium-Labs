# Selenium Labs

This repository contains Python scripts for Selenium automation labs.

## Lab 4: Automated Form Submissions

### Objective

Automate filling and submitting a login form on a practice website and store the data in an AWS RDS MySQL database.

Setup





Install dependencies: pip install -r requirements.txt



Ensure Google Chrome and ChromeDriver are installed.



Update form_submission.py with your AWS RDS credentials.



Run the script: python form_submission.py

Files





form_submission.py: Script to automate form submission and store data in RDS.



requirements.txt: Python dependencies.



.gitignore: Excludes unnecessary files (e.g., .pyc, logs).

Notes





Ensure your RDS security group allows connections from your local IP on port 3306.



Replace placeholders in form_submission.py with your RDS endpoint, username, password, and database name.
