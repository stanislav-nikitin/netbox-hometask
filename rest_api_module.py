#!/usr/bin/python3
# -*- coding: utf-8 -*-

from black import format_file_contents
import requests
from config import *
from requests import HTTPError
from requests import JSONDecodeError
from requests import ConnectionError

# token = "8508d0100ee2f0a3925bbd83d4706a1edf9172f"
# headers = {"Accept": "application/json", "Authorization": "Token " + token}
# url = "https://netbox.vvv"


def rest_api_get(api_call):
    """

    The function is sending REST API GET requests
    Required value: api_call is NetBox API call in fromat "/api/dcim/devices/"

    The function return API response in json (dict)

    """
    try:
        r = requests.get(url + api_call, headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            print("HTTP Error Code:", r.status_code)
            return False

    except HTTPError as error:
        print(error)
        return False

    except JSONDecodeError as error:
        print("JSONDecodeError: [Errno Expecting value] <!doctype html>")
        return False

    except ConnectionError as error:
        print(
            "ConnectionError: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known"
        )
        return False


def rest_api_put(api_call, data):
    """

    The function is sending REST API PUT requests

    Required value:
     - api_call is NetBox API call in fromat "/api/dcim/devices/"
     - data (json)

    The function return API response in json (dict)

    """
    try:
        r = requests.put(url + api_call, headers=headers, json=data)
        if r.status_code == 200:
            return r.json()
        else:
            print("HTTP Error Code:", r.status_code)
            return False

    except HTTPError as error:
        print(error)
        return False

    except JSONDecodeError as error:
        print("JSONDecodeError: [Errno Expecting value] <!doctype html>")
        return False

    except ConnectionError as error:
        print(
            "ConnectionError: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known"
        )
        return False


def get_devices_from_netbox():
    """

    The function is colleting device information from Netbox with values:
    Tenant == NOC
    Status of devce = Active

    The function return a list of disctionaries with device values
    """

    api_call = "/api/dcim/devices/?tenant=noc&status=active"
    print("Connection to NETBOX...")
    data = rest_api_get(api_call)

    if data:
        return data["results"]
    else:
        return False


def update_sw_version(devices):
    api = "/api/dcim/devices/"

    for d in devices:
        update_data = {
            "name": d["name"],
            "device_type": {"id": d["device_type"]["id"]},
            "device_role": {"id": d["device_role"]["id"]},
            "tenant": {"id": d["tenant"]["id"]},
            "site": {"id": d["site"]["id"]},
            "custom_fields": {"sw_version": d["custom_fields"]["sw_version"]},
        }
        api_call = api + str(d["id"]) + "/"  # "/api/dcim/devices/{id}/"
        rest_api_put(api_call, update_data)

    return True
