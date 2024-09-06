#!/bin/bash

# Download ChromeDriver
wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip -P /home/site/wwwroot/
unzip /home/site/wwwroot/chromedriver_linux64.zip -d /home/site/wwwroot/
rm /home/site/wwwroot/chromedriver_linux64.zip

# Set PATH environment variable
export PATH=$PATH:/home/site/wwwroot

# Run main.py
python /home/site/wwwroot/main.py
chmod +x /home/site/wwwroot/main.py