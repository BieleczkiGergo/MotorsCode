#! /bin/python3

import smbus

bus = smbus.SMBus(1)

for addr in range(256):
    data = bus.read_byte_data(address, 0x00)
    print(f"Data: {data}")

