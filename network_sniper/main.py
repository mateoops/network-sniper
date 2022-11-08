import click
from port_checker import port_checker
from helpers import generate_ip_network, validate_data
import threading
import time

@click.command()
@click.option('--network', help = 'Network address with mask eg. 192.168.1.0/24')
@click.option('--port_range_from', help = 'Port range from')
@click.option('--port_range_to', help = 'Port range to')

def scan_network(network, port_range_from, port_range_to):

    # This function is using for scan open ports in whole network
    # Params are provided by click
    # Result are printing to the console

    # validate parameters
    validate_data(network, port_range_from, port_range_to)

    # list of scans - to run in threads
    scan_list = []
    # counter of started scans
    counter = 0

    # generate list of sockets to scan
    for ip in generate_ip_network(network):
        for port in range(int(port_range_from), int(port_range_to)):
            scan_list.append(threading.Thread(target=port_checker, args=(format(ip), port)))
            
    # scan
    for scan in scan_list:
        counter += 1
        scan.start()
        # it stop makes new scans for 1 second
        # it is necessary to not create too many threads
        if counter % 1000 == 0:
            time.sleep(1)

if __name__ == '__main__':
    scan_network()