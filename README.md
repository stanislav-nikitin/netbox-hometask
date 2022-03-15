## netbox sw upgrade script 
Verstion 0.0.2

## Task

Write an application that would collect information directly from the network devices, and update custom field in Netbox for each device.

- Use https://netboxdemo.com/ and https://master.netbox.dev as an example of Netbox environment. Recommendation to spin up your Netbox environment for easier development
-nCollect information for devices with Status = Active, Tenant = NOC in Netbox
- Information to collect: software version
- Custom field to update: "sw_version"

## Usage

The script is using Token Auth for Rest API and pre-defined URL.
Need to define values at "config.py"

### Pre Requirements:
- IP addresses of the devices are takin from NetBox ("Primary IPv4")
- "sw_upgrade" customer field has type "Text(long)"
- SSH is comfigured
- You can connect by using same pair login/password

### Usage example: 
```
supermegaroot% python3.9 sw_info_update.py
Connection to NETBOX...
################################################################ 
Name:  dmi01-akron-rtr01 
IP:  10.48.62.252/24 
SW Version:  None
################################################################


Please input user credentials

Username: test
Password: 
################################################################
Connection to device 10.48.62.252...

Software Version:
 17.05.01a

Software information update succesfull
Connection to NETBOX...
################################################################

Software versions after updating attempt:

################################################################ 
Name:  dmi01-akron-rtr01 
IP:  10.48.62.252/24 
SW Version:  17.05.01a
```
## SNMP
- There were ideas to collect software version by using SNMP & sysDescr OID (snmp_module.py)
- I did not deploy aruba/palo alto devices, but based on searching in the [internet](https://live.paloaltonetworks.com/t5/general-topics/snmp-oid-s/td-p/14373) Palo Alto do not show software version vis  the output

## Test coverage
- unit tests cover only connectivity functions at the current version
