import json
from functools import reduce
from operator import truediv

from scapy import all as scapy

from jsonpkt.commands import BaseCommand


class SendCommand(BaseCommand):
    def process(self, args):
        file = args.file
        pkt_json = {}
        with open(file) as fp:
            pkt_json = json.load(fp)
        packets = []
        pkt_type = next(iter(pkt_json), None)
        while pkt_type:
            pkt = pkt_json.get(pkt_type, {})
            payload = pkt.pop('payload', {})
            scapy_pkt = getattr(scapy, pkt_type, None)
            if scapy_pkt:
                packets.append(scapy_pkt(**pkt))
            pkt_json = payload
            pkt_type = next(iter(pkt_json), None)
        send_packet = reduce(truediv, packets)
        print(send_packet.show())
        scapy.srp(send_packet)
        
