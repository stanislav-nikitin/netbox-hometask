#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Rest API
token = "84ca7eb944ea0a5842b0c21d316750900641fdc0"
headers = {"Accept": "application/json", "Authorization": "Token " + token}
url = "https://demo.netbox.dev"

# SNMP:
oid = ["1.3.6.1.2.1.1.1.0"]
community = "public"
