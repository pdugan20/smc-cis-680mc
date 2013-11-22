#!/usr/local/bin/python3 -u  
# -u turns off output buffering
# Creator: patdugan
# File: python_logo.py
# Description: return a binary file to stdout (the web server)

# We need the sys module for this job
import sys

# Read binary data with ’rb’
data = open('/home/students/patridugan/public_html/images/python-logo-master-v3-TM-flattened.png','rb').read()

# Print image/png media type, and number of characters sent
print("Content-Type: image/png\nContent-Length: %d\n" % len(data))

# Print binary data to stdout
sys.stdout.buffer.write(data)
