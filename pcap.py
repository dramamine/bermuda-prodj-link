# import pcap
# sniffer = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=50)


# def addr(pkt, offset): return '.'.join(
#     str(ord(pkt[i])) for i in range(offset, offset + 4))


# for ts, pkt in sniffer:
#   print('%d\tSRC %-16s\tDST %-16s' % (ts, addr(pkt, sniffer.dloff + 12), addr(pkt, sniffer.dloff + 16)))


import npcap
import socket


def forward_traffic(source_port, destination_port):
  # Create a raw socket to capture traffic from the source port
  source_socket = socket.socket(
      socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
  source_socket.bind(('localhost', source_port))

  # Create a raw socket to forward traffic to the destination port
  destination_socket = socket.socket(
      socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
  destination_socket.bind(('localhost', destination_port))

  # Start forwarding traffic
  while True:
    packet = source_socket.recv(65535)
    destination_socket.send(packet)


# Usage: forward_traffic(source_port, destination_port)
forward_traffic(50001, 50003)
