import ipaddress

def split_ip_mask(ip_with_mask):

    # This function returns dictionary with network and mask keys
    # from string in format 0.0.0.0/0

    return_dict = {
        "network":  str(ip_with_mask.split('/')[0]),
        "mask":     int(ip_with_mask.split('/')[1])
    }
    return return_dict

def generate_ip_network(network_with_mask_string = '10.20.30.0/24'):

    # This function returns list of IP addresses from string in format 0.0.0.0/0

    ips = []
    for ip in ipaddress.IPv4Network(network_with_mask_string):
        ips.append(ip)
    return ips

def validate_data(network, range_ports):

    # This function validates data provided by Click

    if network == None:
        raise Exception('--network param not provided!')
    try:
        generate_ip_network(network)
    except:
        raise Exception('Incorrect --network param!')
    try:
        port_range_from = int(range_ports.split('-')[0])
        port_range_to = int(range_ports.split('-')[1])
    except:
        raise Exception('Incorrect ports range param!')
    try:
        if int(port_range_from) > int(port_range_to):
            raise Exception('Incorrect ports range param!')
        if int(port_range_from) < 1 or int(port_range_from) > 65535:
            raise Exception('Incorrect ports range param')
        if int(port_range_to) < 1 or int(port_range_to) > 65535:
            raise Exception('Incorrect ports range param')

    except Exception as ex:
        raise ex