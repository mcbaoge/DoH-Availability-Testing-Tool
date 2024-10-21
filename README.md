# DoH-Availability-Testing-Tool.
This tool checks the availability of various DNS over HTTPS (DoH) service providers. It queries a specified domain and reports which providers are accessible from the current network environment.

Features
Tests multiple DoH service providers
Displays results in a user-friendly GUI
Provides detailed feedback on the availability of each provider
Requirements
Python 3.x
tkinter library (usually included with Python)
requests library
concurrent.futures library (usually included with Python)
Installation
Ensure you have Python 3.x installed on your system.
Install the required libraries if they are not already installed:
pip install requests

Usage
Save the provided code into a Python file, e.g., doh_availability_tool.py.
Run the script:
python doh_availability_tool.py

Click the “开始监测” button to start monitoring the availability of DoH providers.
