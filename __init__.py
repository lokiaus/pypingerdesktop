from core import *


if __name__ == '__main__':

    logging.info(f"{time.asctime(time.localtime())}  Pinger started")

    while True:
        print(f"Pinging...")
        ping_data = avg_ping("google.com", 20)

        if ping_data['Success']:
            print(f"Min/Max/Avg RTT = {ping_data['MinRTT']} / {ping_data['MaxRTT']} / {ping_data['AvgRTT']}, "
                  f"Packet Loss = {ping_data['PacketLoss']}%")
        else:
            print("Ping failed!")

        logging.info(f"{time.asctime(time.localtime())}  "
                     f"Min/Max/Avg RTT = {ping_data['MinRTT']} / {ping_data['MaxRTT']} / {ping_data['AvgRTT']}  "
                     f"Packet Loss: {ping_data['PacketLoss']}%  "
                     f"Success: {ping_data['Success']}")
        time.sleep(5)
