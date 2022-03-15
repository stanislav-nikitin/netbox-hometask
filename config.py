#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Rest API
token = "321ef4a14021de79150b022976dd7006a7757698"
headers = {"Accept": "application/json", "Authorization": "Token " + token}
url = "https://demo.netbox.dev"

# SNMP:
oid = ["1.3.6.1.2.1.1.1.0"]
community = "public"
