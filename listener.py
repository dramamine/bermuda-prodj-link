from scapy.all import sniff, UDP, IP, hexdump
from scapy.all import get_if_list

# len(pkt) > 100 and len(pkt) < 150 and
def packet_printer(pkt):
  if pkt.dst == 'ff:ff:ff:ff:ff:ff':
    print("Broadcast packet: %s" % pkt.summary())
  # hexdump(pkt)
  if pkt[IP].src == '169.254.8.208':
    print("Broadcast packet: %s" % pkt.summary())
  if pkt.haslayer(UDP):
    print("Broadcast packet: %s" % pkt.summary())

  #   print("Packet length: %s" % len(pkt))
  #   print(pkt.show())

# pick the Ethernet interface (not the wifi one)


# Capture network packets using Scapy's sniff() function
packets = sniff(prn=packet_printer, filter="ip")

# list interfaces
# interfaces = get_if_list()
# print("Available interfaces:")
# for interface in interfaces:
#   print(interface)
#   print(interface.pcap_name)
