import click
from port_checker import port_checker
from helpers import generate_ip_network, validate_data
import threading
import time

@click.command()
@click.option('--network', help = 'Network address with mask eg. 192.168.1.0/24')
@click.option('--port_range_from', help = 'Port range from')
@click.option('--port_range_to', help = 'Port range to')

def test(network, port_range_from, port_range_to):

    scan_list = []
    counter = 0

    validate_data(network, port_range_from, port_range_to)

    for ip in generate_ip_network(network):
        for port in range(int(port_range_from), int(port_range_to)):
            scan_list.append(threading.Thread(target=port_checker, args=(format(ip), port)))
    for scan in scan_list:
        counter += 1
        scan.start()
        if counter % 1000 == 0:
            time.sleep(1)

if __name__ == '__main__':
    test()