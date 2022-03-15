import pytest
import rest_api_module
import sys


def test_function_rest_api_get_connection_error(capsys, wrong_url):
    return_value = rest_api_module.rest_api_get(wrong_url)

    correct_stdout1 = "JSONDecodeError"
    correct_stdout2 = "ConnectionError"
    correct_stdout3 = "HTTPError"
    correct_stdout4 = "HTTP Error Code: 403"

    out, err = capsys.readouterr()

    assert return_value == False

    assert out != "", "Error message wasn't print stdout"
    assert (
        correct_stdout1 in out
        or correct_stdout2 in out
        or correct_stdout3 in out
        or correct_stdout4 in out
    ), "Wrong error message had been printer to stdout"


def test_function_rest_api_put_connection_error(capsys, wrong_url, rest_api_bad_data):

    return_value = rest_api_module.rest_api_put(wrong_url, rest_api_bad_data)

    correct_stdout1 = "JSONDecodeError"
    correct_stdout2 = "ConnectionError"
    correct_stdout3 = "HTTPError"
    correct_stdout4 = "HTTP Error Code: 403"

    out, err = capsys.readouterr()

    assert return_value == False

    assert out != "", "Error message wasn't print stdout"
    assert (
        correct_stdout1 in out
        or correct_stdout2 in out
        or correct_stdout3 in out
        or correct_stdout4 in out
    ), "Wrong error message had been printer to stdout"


def test_function_rest_api_put_wrong_data(capsys, valid_put_req, rest_api_bad_data):

    return_value = rest_api_module.rest_api_put(valid_put_req, rest_api_bad_data)

    correct_stdout1 = "HTTP Error Code"

    out, err = capsys.readouterr()

    assert return_value == False

    assert out != "", "Error message wasn't print stdout"
    assert correct_stdout1 in out, "Wrong error message had been printer to stdout"


def test_function_get_devices_from_netbox(capsys):
    return_value = rest_api_module.get_devices_from_netbox()

    assert return_value is not None
    assert type(return_value) is list
    assert type(return_value[0]) is dict


def test_function_update_sw_version_good_dataset(capsys, devices_good_dataset):
    return_value = rest_api_module.update_sw_version(devices_good_dataset)

    assert devices_good_dataset is not None
    assert type(devices_good_dataset) is list
    assert type(devices_good_dataset[0]) is dict

    assert return_value is True

    assert devices_good_dataset[0]["name"] is not None
    assert devices_good_dataset[0]["device_role"]["id"] is not None
    assert devices_good_dataset[0]["tenant"]["id"] is not None
    assert devices_good_dataset[0]["site"]["id"] is not None
    assert devices_good_dataset[0]["device_type"]["id"] is not None
