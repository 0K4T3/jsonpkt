import os
import unittest

from jsonpkt import utils

from scapy import all as scapy


class TestUtils(unittest.TestCase):
    def test_replace_with_environment_var_by_no_environment_var(self):
        test_value = 'test'
        result = utils.replace_with_environment_var(test_value)
        expected  = 'test'
        self.assertEqual(result, expected)

    def test_replace_with_environment_var_by_environment_var(self):
        os.environ['TEST'] = 'test'
        test_value = '${TEST}'
        result = utils.replace_with_environment_var(test_value)
        expected = 'test'
        self.assertEqual(result, expected)

    def test_parse_packet_json(self):
        test_packet_json = {
            'Ether': {
                'src': 'dummy_src_mac_addr',
                'dst': 'dummy_dst_mac_addr',
            }
        }
        result = utils.parse_packet_json(test_packet_json)
        expected = scapy.Ether(src='dummy_src_mac_addr', dst='dummy_dst_mac_addr')
        self.assertEqual(result, expected)

    def test_parser_packet_json_use_env_var(self):
        os.environ['DUMMY_SRC_MAC_ADDR'] = 'dummy_src_mac_addr'
        os.environ['DUMMY_DST_MAC_ADDR'] = 'dummy_dst_mac_addr'
        test_packet_json = {
            'Ether': {
                'src': '${DUMMY_SRC_MAC_ADDR}',
                'dst': '${DUMMY_DST_MAC_ADDR}',
            }
        }
        result = utils.parse_packet_json(test_packet_json)
        expected = scapy.Ether(src='dummy_src_mac_addr', dst='dummy_dst_mac_addr')
        self.assertEqual(result, expected)

    def test_to_packet_json(self):
        test_packet = scapy.Ether(src='dummy_src_mac_addr', dst='dummy_dst_mac_addr')/scapy.IP(src='192.168.0.10', dst='192.168.0.1')
        result = utils.to_packet_json(test_packet)
        expected = {
            'Ether': {
                'src': 'dummy_src_mac_addr',
                'dst': 'dummy_dst_mac_addr',
                'payload': {
                    'IP': {
                        'src': '192.168.0.10',
                        'dst': '192.168.0.1',
                    },
                },
            },
        }
        self.assertEqual(result, expected)
