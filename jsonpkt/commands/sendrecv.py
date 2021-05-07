import json

from scapy import all as scapy

from jsonpkt.commands import BaseCommand
from jsonpkt.utils import parse_packet_json, to_packet_json


class SendRecvCommand(BaseCommand):
    def process(self, args):
        file = args.file
        with open(file) as fp:
            packet_json = json.load(fp)
            packet = parse_packet_json(packet_json)
            res = scapy.sr1(packet, verbose=False)
            packet_json = to_packet_json(res)
            print(json.dumps(packet_json, indent=2))
