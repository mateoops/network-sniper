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

def validate_data_and_generate_ports_list(network, ports_range, ports_list):

    # This function validates data provided by Click
    # and returns list of ports

    list_of_ports = []

    if network == None:
        raise Exception('--network param not provided!')
    try:
        generate_ip_network(network)
    except:
        raise Exception('Incorrect --network param!')
    
    # Ports provided by ports_range
    if ports_range != None and ports_list == None:

        try:
            port_range_from = int(ports_range.split('-')[0])
            port_range_to = int(ports_range.split('-')[1])
        except:
            raise Exception('Incorrect ports range param!')

        try:
            if int(port_range_from) > int(port_range_to):
                raise Exception('Incorrect ports range param!')
            if int(port_range_from) < 1 or int(port_range_from) > 65535:
                raise Exception('Incorrect ports range param')
            if int(port_range_to) < 1 or int(port_range_to) > 65535:
                raise Exception('Incorrect ports range param')
            else:
                list_of_ports = list(range(int(ports_range.split('-')[0]), int(ports_range.split('-')[1])+1))
                return list_of_ports
        except Exception as ex:
            raise ex

        

    # Ports provided by ports_list
    elif ports_range == None and ports_list != None:
        try:
            list_of_ports_string = str(ports_list).split(',')
        except:
            raise Exception('Incorrect ports list')
        if len(list_of_ports_string) < 1:
            raise Exception('Incorrect ports list')
        else:
            try:
                for port in list_of_ports_string:
                    if int(port) < 1 or int(port) > 65535:
                        raise Exception('Incorrect ports range param')
                    else:
                        list_of_ports.append(int(port))
                return list_of_ports
            except:
                raise Exception('Incorrect ports range param')
    else:
        raise Exception('Too many parameters! Choose only one type of input ports')