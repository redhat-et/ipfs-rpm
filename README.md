# ipfs-rpm
The IPFS RPM is generated and stored in copr. Currently, the RPM is available for Centos 8 and RHEL 8.

## Installation
To install the RPM on your system perform the following.

```
dnf copr enable @redhat-et/ipfs
dnf -y install kubo
```

## Starting IPFS
A systemd file is deployed on the system by the rpm. Before running IPFS needs to init.

```
ipfs init
```

Once this has been the systemd service can be started.

```
systemctl enable ipfs --now
```
