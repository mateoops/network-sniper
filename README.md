# network-sniper

Python network scanner tool, with additional network features.

## Usage

```shell
Usage:
    python network_sniper/main.py <networkAddressWithMask> --range_ports <lowerPort>-<higherPort>
    python network_sniper/main.py --help

Options:
    --help              Show this screen
    --network           Network address with mask. Format: 0.0.0.0/0
    --range_ports       Define range of ports to scan
```
## Examples
Scan range between 1 to 80 ports in network 192.168.10.0/24

```shell
python network_sniper/main.py --network 192.168.10.0/24 --range_ports 1-80
```