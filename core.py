import time
import logging
from ping3 import ping

logging.basicConfig(filename='pinger.log', encoding='utf-8', level=logging.DEBUG)


def avg_ping(target_host, count=5):
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
        time.sleep(0.5)

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
            'AvgRTT': "0ms",
            'MaxRTT': "0ms",
            'MinRTT': "0ms",
            'PacketLoss': 100,
            'Success': False,
        }
