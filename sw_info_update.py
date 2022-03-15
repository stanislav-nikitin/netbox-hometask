#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ipaddress
import getpass
import re

from rest_api_module import *
from netmiko_module import send_show_command


def get_ip(int_ip_prefix):
    """
    The function is expect value "int_ip_prefix":
    IP address from Netbox in a format: "x.x.x.x/y"

    The function is return IP in string format: "x.x.x.x"
    """
    return str(ipaddress.ip_interface(int_ip_prefix).ip)


def get_device_cred():
    """
    The functioin allow to get device credentials

    The function return a disctionary {"username": "xxx", "password": "yyy"}
    """
    cred = {}
    print("#####################################################################\n")
    print("\nPlease input user credentials\n")
    cred["username"] = input("Username: ")
    cred["password"] = getpass.getpass()
    print("####################################################################\n")
    return cred


def parse_sh_version(output):

    regex = "[Vv]ersion.(\d.*)"
    match = re.search(regex, output)

    return match.group(1)


def get_sw_version_netmiko(devices):
    """

    The function is collecting sw version of devices by using Netmiko.

    Expect: list of devices collected from Netbox


    Suppose:
        - device credentials the same for all devices
        - device_type is using "autodetect" to simplify a connections

    Return: modified list of devices with up-to-dated values for "sw_version" in "custome_fields"
    """
    command = "show version"
    dev_paramset = {
        "device_type": "autodetect",
    }
    dev_paramset.update(get_device_cred())

    for d in devices:
        print("################################################################")

        dev_paramset["ip"] = get_ip(d["primary_ip"]["address"])
        print(dev_paramset)

        output = send_show_command(dev_paramset, command)

        if output:
            sh_ver = parse_sh_version(output)
            d["custom_fields"]["sw_version"] = sh_ver
            print("\nSoftware Version:\n", sh_ver)

    return devices


def print_collected_devices_from_netbox(devices):
    for device in devices:
        if device["primary_ip"]:
            print(
                "################################################################",
                "\nName: ",
                device["name"],
                "\nIP: ",
                device["primary_ip"]["address"],
                "\nSW Version: ",
                device["custom_fields"]["sw_version"],
            )


if __name__ == "__main__":
    d1 = get_devices_from_netbox()
    print_collected_devices_from_netbox(d1)

    update_sw_version(get_sw_version_netmiko(d1))
    # get_sw_version(devices)

    d2 = get_devices_from_netbox()
    print_collected_devices_from_netbox(d2)
