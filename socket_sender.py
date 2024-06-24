import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(("127.0.0.1", 60000))

try:
  while True:
    sock.sendto('hello'.encode(), ("127.0.0.1", 60000))
    print("sent")
    # wait 5 seconds.
    time.sleep(5)
except KeyboardInterrupt:
  pass
