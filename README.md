## Task

Write an application that would collect information directly from the network devices, and update custom field in Netbox for each device.

> Use https://netboxdemo.com/ and https://master.netbox.dev as an example of Netbox environment. Recommendation to spin up your Netbox environment for easier development
> Collect information for devices with Status = Active, Tenant = NOC in Netbox
> Information to collect: software version
> Custom field to update: "sw_version"

===
The script is using Token Auth for Rest API and pre-defined URL.
Need to define values at "config.py"
