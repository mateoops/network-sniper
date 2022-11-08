import ipaddress

def split_ip_mask(ip_with_mask):
    return_dict = {
        "network":  str(ip_with_mask.split('/')[0]),
        "mask":     int(ip_with_mask.split('/')[1])
    }
    return return_dict

def generate_ip_network(network_with_mask_string = '10.20.30.0/24'):
    ips = []
    for ip in ipaddress.IPv4Network(network_with_mask_string):
        ips.append(ip)
    return ips

def validate_data(network, port_range_from, port_range_to):
    if network == None:
        raise Exception('--network param not provided!')
    try:
        generate_ip_network(network)
    except:
        raise Exception('Incorrect --network param!')
    try:
        int(port_range_from)
        int(port_range_to)
    except:
        raise Exception('Incorrect ports range params!')
    try:
        if int(port_range_from) > int(port_range_to):
            raise Exception('Param --port_range_from should be lower or equal --port_range_to param!')
        if int(port_range_from) < 1 or int(port_range_from) > 65535:
            raise Exception('Param port_range_from must be greater than 0 and lower than 65535')
        if int(port_range_to) < 1 or int(port_range_to) > 65535:
            raise Exception('Param port_range_to must be greater than 0 and lower than 65535')

    except Exception as ex:
        raise ex