from core import *


if __name__ == '__main__':

    logging.info(f"{time.asctime(time.localtime())}  Pinger started")

    while True:
        asyncio.run(main())
