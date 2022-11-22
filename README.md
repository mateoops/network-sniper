# network-sniper

Python network scanner tool, with additional network features.

## Usage

```shell
Usage:
    python network_sniper/main.py --network <networkAddressWithMask> --ports_range <lowerPort>-<higherPort>
    python network_sniper/main.py --network <networkAddressWithMask> --ports_list <port1,port2,port3...>
    python network_sniper/main.py --network <networkAddressWithMask> --port <port>
    python network_sniper/main.py --help

Options:
    --help              Show this screen
    --network           Network address with mask. Format: 0.0.0.0/0
    --port              Port number to scan
    --ports_range       Define range of port numbers to scan
    --ports_list        Define port numbers in list. Format (e.g.) 80,443,8080,8443
```
## Examples
Scan range between 1 to 80 ports in network 192.168.10.0/24

```shell
python network_sniper/main.py --network 192.168.10.0/24 --ports_range 1-80
```

Scan ports 22, 80, 443 on host 192.168.10.6/32

```shell
python network_sniper/main.py --network 192.168.10.6/32 --ports_list 22,80,443
```

Scan port 53 on host in network 10.10.0.0/16

```shell
python network_sniper/main.py --network 10.10.0.0/16 --port 53
```