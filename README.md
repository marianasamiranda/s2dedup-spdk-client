# S2Dedup's Client

This repository is part of the S2Dedup project. Please refer to [S2Dedup repository](https://github.com/mmm97/S2Dedup) for further information. 

S2Dedup's client implementation is based on the Storage Performance Development Kit ([SPDK](http://www.spdk.io)), which provides a set of tools and libraries for writing high performance, scalable, user-mode storage applications. Please refer to ([SPDK-Getting_Started](https://spdk.io/doc/getting_started.html)) for installation instructions.

SPDK features an iSCSI client virtual block device that integrates [libiscsi](https://github.com/sahlberg/libiscsi), which allows clients to connect and transfer data to a remote storage system ([S2Dedup server](https://github.com/mmm97/s2dedup-spdk-server.git)) through the iSCSI protocol. Also, to provide a standard block-device interface for client applications (e.g., filesystem), an SPDK Linux NBD driver was stacked on top of the iSCSI client block device. 

In order to offer client side encryption, SPDK's implementation was extended to provide transparent data encryption with the AES-XTS block cipher mode. 

After the installation, at [init_iscsi_initiator.sh](init_iscsi_initiator.sh)  we have an example on how the S2Dedup's client can be initiated:
~~~{.sh}
sudo ./scripts/rpc.py bdev_iscsi_create -b iSCSI0 -i iqn.2016-06.io.spdk:Target --url iscsi://192.168.112.129:3260/iqn.2016-06.io.spdk:Target/0

#do not forget to do sudo modprobe nbd
sudo ./scripts/rpc.py nbd_start_disk iSCSI0 /dev/nbd0
~~~
