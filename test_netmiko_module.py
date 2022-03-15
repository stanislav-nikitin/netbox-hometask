import pytest
import netmiko_module
import sys


def test_function_wrong_ip(capsys, first_router_wrong_ip):
    return_value = netmiko_module.send_show_command(first_router_wrong_ip, "sh ver")

    correct_stdout1 = "Connection to device timed-out"
    correct_stdout2 = "TCP connection to device failed"

    out, err = capsys.readouterr()

    assert out != "", "Error message wasn't print stdout"
    assert (
        correct_stdout1 in out or correct_stdout2 in out
    ), "Wrong error message had been printer to stdout"


def test_function_wrong_pass(capsys, first_router_wrong_pass):
    return_value = netmiko_module.send_show_command(first_router_wrong_pass, "sh ver")

    correct_stdout = "Authentication fail"
    out, err = capsys.readouterr()

    assert out != "", "Error message wasn't print stdout"
    assert correct_stdout in out, "Wrong error message had been printer to stdout"
