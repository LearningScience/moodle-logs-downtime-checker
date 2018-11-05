# Moodle Log File Downtime Checker
Use this script to check for possible downtime/outages in your Moodle logs.

Note: This is not full proof, it only checks Moodle user activity logs. If you have access to them web server logs will be far more accurate.

## Usage
1. Download Moodle logs by logging in as an admin > Site Administration > Reports > Logs. Use the dropdown menus to select a day, and click Get these logs. When the logs have finished generating, click Download table data as .csv.
2. Run the script using `python check-downtime.py -f ./path/to/logs.csv -m <minutes downtime>`.
