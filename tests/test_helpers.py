import unittest
from network_sniper.helpers import generate_ip_network, split_ip_mask

class TestHelpers(unittest.TestCase):

    ### generate_ip_network function tests

    def test_check_ips_are_list(self):
        ips = generate_ip_network()
        self.assertEqual(ips.__class__, [].__class__)

    def test_check_ips_count(self):
        ips = generate_ip_network('192.168.192.0/24')
        self.assertEqual(len(ips), 256)

    def test_check_ips_elements(self):
        ips = generate_ip_network('192.168.192.0/24')
        self.assertEqual(str(ips[0]), '192.168.192.0')
        self.assertEqual(str(ips[33]), '192.168.192.33')
        self.assertEqual(str(ips[len(ips)-1]), '192.168.192.255')

    ### split_ip_mask function tests

    def test_split_ip_mask(self):
        split_obj = split_ip_mask('192.168.192.0/24')
        self.assertEqual(split_obj['network'], '192.168.192.0')
        self.assertEqual(split_obj['mask'], 24)

if __name__ == '__main__':
    unittest.main()