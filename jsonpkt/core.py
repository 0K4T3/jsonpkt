import argparse
import sys
from typing import List

from jsonpkt.commands import SendCommand, ViewCommand


argparser = argparse.ArgumentParser()
subparsers = argparser.add_subparsers()

subparser_send = subparsers.add_parser('send', help='Generate and send packet by JSON file. See "jsonpkt send -h"')
subparser_send.add_argument('file', help='Packet definition file. (JSON)')
subparser_send.set_defaults(handler=lambda args: SendCommand().process(args))
subparser_view = subparsers.add_parser('view', help='View packet prettierly. See "jsonpkt view -h"')
subparser_view.add_argument('file', help='Packet definition file. (JSON)')
subparser_view.set_defaults(handler=lambda args: ViewCommand().process(args))


def main(args: List[str] = sys.argv):
    _, *args = args
    parsed_args = argparser.parse_args(args=args)
    parsed_args.handler(parsed_args)
    
