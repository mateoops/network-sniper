# network-sniper

Python network scanner tool, with additional network features.

Usage:
    python network_sniper/main.py <networkAddressWithMask> --port_range_from <port> --port_range_to <port>
    python network_sniper/main.py --help
Options:
    --help              Show this screen.
    --network           Network address with mask. Format: 0.0.0.0/0
    --port_range_from   Define range of ports to scan - from
    --port_range_to     Define range of ports to scan - to

## Examples
Scan range between 1 to 80 ports in network 192.168.10.0/24

```shell
python network_sniper/main.py --network 192.168.10.0/24 --port_range_from 1 --port_range_to 80
```