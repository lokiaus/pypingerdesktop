import time
import logging
from ping3 import ping
import asyncio

logging.basicConfig(filename='pinger.log', encoding='utf-8', level=logging.DEBUG)


async def main():
    choice = input("p/q: ")
    if choice == "p":
        print(f"Pinging...")
        ping_data = await avg_ping("google.com")

        if ping_data['Success']:
            print(f"Min/Max/Avg RTT = {ping_data['MinRTT']} / {ping_data['MaxRTT']} / {ping_data['AvgRTT']}, "
                  f"Packet Loss = {ping_data['PacketLoss']}%")
        else:
            print("Ping failed!")

        logging.info(f"{time.asctime(time.localtime())}  "
                     f"Min/Max/Avg RTT = {ping_data['MinRTT']} / {ping_data['MaxRTT']} / {ping_data['AvgRTT']}  "
                     f"Packet Loss: {ping_data['PacketLoss']}%  "
                     f"Success: {ping_data['Success']}")

        # await asyncio.sleep(15)

    elif choice == "q":
        exit()


async def avg_ping(target_host, count=5):
    """

    Args:
        target_host: Hostname to ping
        count: Number of times hostname will be pinged

    Returns: Dictionary containing average response time and success/failure boolean value

    """
    rtt = []
    nr = 0

    for i in range(count):
        init = ping(target_host, unit='ms')
        if init is None or init is False:
            nr += 1
            # print("No Response")
            logging.warning(f'No Response from {target_host}')
        else:
            rtt.append(init)
            # print(f"{round(rtt[-1], 1)}ms")
            # logging.info(f'Ping received from {target_host} in {round(rtt[-1], 1)}ms')
        await asyncio.sleep(0.2)  # adjust for testing

    if len(rtt) != 0:
        avg_rtt = round(sum(rtt) / len(rtt), 1)
        return {
            'AvgRTT': f"{avg_rtt}ms",
            'MaxRTT': f"{round(max(rtt))}ms",
            'MinRTT': f"{round(min(rtt))}ms",
            'PacketLoss': int(nr / count * 100),
            'Success': True,
        }
    else:
        return {
            'AvgRTT': f"0ms",
            'MaxRTT': f"0ms",
            'MinRTT': f"0ms",
            'PacketLoss': 100,
            'Success': False,
        }
