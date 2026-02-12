#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

apt update
apt install -y python3-pip wget sudo gh cron
pip install -r requirements.txt
(crontab -l ; echo "* * * * * /usr/bin/python3 .devcontainer/heartbeat.py") | sort - | uniq - | crontab -
service cron start