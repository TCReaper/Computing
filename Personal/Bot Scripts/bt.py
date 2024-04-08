import asyncio
import tracemalloc
tracemalloc.start()
from bleak import BleakClient,BleakScanner

device_address = 'c0:86:b3:82:08:31'.upper()

async def connect_to_device(address):
    try:
        async with BleakClient(address) as client:
            await client.connect()
    except Exception as e:
        print("Error occurred:", e)

# Run the asynchronous connection coroutine
asyncio.run(connect_to_device(device_address))

# print(asyncio.run(BleakScanner.discover()))
