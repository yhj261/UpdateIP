#! /usr/bin/python2.7

import logging  # Use logging module to format the log file
import requests # Use request module to send GET request and get external ip
import time     # Use sleep function
from ConfigParser import ConfigParser
from sendmail import sendmail # import the sendmail function we created in sendmail.py

SLEEP_TIME = 60 # 60 seconds interval between each IP check

# Parse the configuration file to get mail-settings
parser = ConfigParser()
parser.read('mail-setting.conf')
smtp_server =  parser.get('mail-setting', 'smtp_server')
port =  parser.get('mail-setting', 'port')
username = parser.get('mail-setting', 'username')
password = parser.get('mail-setting', 'password')
recipient = parser.get('mail-setting', 'recipient')

# Specify log format and set the logging level to INFO
logging.basicConfig(filename='updateip.log',level=logging.INFO,\
format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Get external IP by sending GET request to "icanhanzip.com"
try:
    res = requests.get("http://icanhazip.com")
# If there's no internet connection, print error message and exit 
except requests.exceptions.ConnectionError:
    print "Connection failed, exit"
    logging.error("Connection failed, exit")
    exit(0)
# Send an email containing the initial ip and keep checking for ip changes
else:
    my_ip = res.text.rstrip()
    logging.info("Successfully started, current ip is " \
    + my_ip + ", update cycle is set to " + str(SLEEP_TIME) + " seconds")

    print "Successfully started, current ip is "\
     + my_ip + ", update cycle is set to " + str(SLEEP_TIME) + " seconds"

    sendmail(smtp_server, port, username, password, recipient, \
    "Successfully started, current ip is " + my_ip)
    while True:
        try:
            res = requests.get("http://icanhazip.com")
            curr_ip = res.text.rstrip()
            # If ip changed, send an email notification 
            if (my_ip != curr_ip):
                logging.info("IP changed, current ip is " + curr_ip)
                my_ip = curr_ip
                sendmail(smtp_server, port, username, password, recipient, "current ip is " + curr_ip)
            # When ip stays the same, print a message to log
            else:
                logging.info("IP checked, no change during the last cycle")
        # If network connection lost while the script is running, print an error message to log and retry
        except requests.exceptions.ConnectionError:
            logging.error("Connection lost, retry in " + str(SLEEP_TIME) + " seconds")
        # Sleep for SLEEP_TIME seconds then start next check
        finally:
            time.sleep(SLEEP_TIME)