#!/bin/bash

# Navigate to the directory
cd ../usr/lib/python3.11/site-packages/requests

# Add your key here
key="your_key"

# Modify the file
echo "Bypassing Tool..."
sed -i "/return content/a if self.url == \"https://github.com/BAINXUD/xd/blob/main/prox.txt\":\\
    content = str(\"$key\")" models.py

echo "bypass Successfully!"
