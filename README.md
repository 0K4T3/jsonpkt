# jsonpkt
jsonpkt is a command line tool for generate and send network packet with JSON file.


## Getting started
jsonpkt use scapy internally. So JSON schema is follow scpay packet specification.
like this. (This is sample of simple ICMP packet.)
```
simple-icmp.json
{
  "IP": {
    "dst": "192.168.0.1",
    "payload": {
      "ICMP": {}
    }
  }
}
```

To send packet. (need root privilege)
```
$ python -m jsonpkt send simple-icmp.json
```

To send packet and receive response. (need root privilege)
```
$ python -m jsonpkt sendrecv simple-icmp.json
```

To view packet. (with scapy format)
```
$ python -m jsonpkt view simple-icmp.json
```


## Help
- send
```
usage: -m send [-h] [-l LAYER] file

positional arguments:
  file                  Packet definition file. (JSON)

optional arguments:
  -h, --help            show this help message and exit
  -l LAYER, --layer LAYER
                        Packet layer.
```

- sendrecv
```
usage: -m sendrecv [-h] [-l LAYER] file

positional arguments:
  file                  Packet definition file. (JSON)

optional arguments:
  -h, --help            show this help message and exit
  -l LAYER, --layer LAYER
                        Packet layer.
```

- view
```
usage: -m view [-h] [-f FORMAT] [-i INDENT] file

positional arguments:
  file                  Packet definition file. (JSON)

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Output format.
  -i INDENT, --indent INDENT
                        Indent width. (using format "json")
```
