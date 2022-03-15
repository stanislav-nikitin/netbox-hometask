#!/usr/bin/python3
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException
from netmiko.ssh_exception import SSHException


def send_show_command(device, command):
    """
    The function is connecting via SSH up to device and execute command

    Parameters:
    - device - dictionary with param-set for connection
    - command - command

    The function will return an output of command
    """

    print("Connection to device {}...".format(device["ip"]))

    try:
        with ConnectHandler(**device) as ssh:
            return ssh.send_command(command)

    except NetMikoAuthenticationException as error:
        print(error)
        return False

    except NetMikoTimeoutException as error:
        print(error)
        return False

    except SSHException as error:
        print(error)


"""
the way how to use autodect of device network type:
https://ktbyers.github.io/netmiko/docs/netmiko/ssh_autodetect.html#netmiko.ssh_autodetect.SSHDetect.autodetect

from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler

remote_device = {
    "device_type": "autodetect",
    "host": "remote.host",
    "username": "test",
    "password": "test",
}

guesser = SSHDetect(**remote_device)
best_match = guesser.autodetect()  #network type of the device
"""
