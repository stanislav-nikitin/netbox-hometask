import pytest
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def test_router():
    r1 = {
        "device_type": "autodetect",
        "password": "sddfUGp1.",
        "username": "admin",
        "ip": "192.168.77.249",
    }
    return r1


@pytest.fixture(scope="module")
def first_router_wrong_pass(test_router):
    r1 = test_router.copy()
    r1["password"] = "wrong"
    return r1


@pytest.fixture(scope="module")
def first_router_wrong_ip(test_router):
    r1 = test_router.copy()
    r1["ip"] = "169.254.1.1"
    return r1


@pytest.fixture(scope="module")
def wrong_url():
    url = "https://dddd.netbox.dev"
    return url


@pytest.fixture(scope="module")
def valid_put_req():
    url = "/api/dcim/devices/115/"
    return url


@pytest.fixture(scope="module")
def rest_api_bad_data():
    data_test = {
        "name": "noc-akron-rtr01",
        "device_type": {"id": 6},
        "custom_fields": {"sw_version": "17.6.1.1"},
    }
    return data_test


@pytest.fixture(scope="module")
def devices_good_dataset():
    list = []
    data_test = {
        "name": "noc-akron-rtr01",
        "device_type": {"id": 6},
        "device_role": {"id": 1},
        "tenant": {"id": 14},
        "site": {"id": 15},
        "custom_fields": {"sw_version": "17.6.5.1"},
        "id": 115,
    }
    list.append(data_test)
    return list


@pytest.fixture(scope="module")
def devices_bad_dataset():
    list = []
    data_test = {
        "id": 115,
        "name": "noc-akron-rtr01",
        "device_type": {"id": 6},
    }
    list.append(data_test)
    return list
