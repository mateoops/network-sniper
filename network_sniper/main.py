import click
from port_checker import port_checker
from helpers import generate_ip_network, validate_data_and_generate_ports_list
import threading
import time

@click.command()
@click.option('--network',      help = 'Network address with mask eg. 192.168.1.0/24')
@click.option('--ports_range',  help = 'Port numbers range to scan')
@click.option('--ports_list',   help = 'Port numbers list to scan')
@click.option('--port',         help = 'Single port number to scan')

def scan_network(network, ports_range, ports_list, port):

    # This function is using for scan open ports in whole network
    # Params are provided by click
    # Result are printing to the console

    # validate parameters
    list_of_ports = validate_data_and_generate_ports_list(network, ports_range, ports_list, port)

    # list of scans - to run in threads
    scan_list = []
    # counter of started scans
    counter = 0

    # generate list of sockets to scan
    for ip in generate_ip_network(network):
        for port in list_of_ports:
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