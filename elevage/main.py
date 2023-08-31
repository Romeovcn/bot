import time
import threading
from srcs.bot import check_exit_thread
from srcs.bot import main_bot_thread

if __name__ == "__main__":
    time.sleep(2)

    thread_1 = threading.Thread(target=check_exit_thread)
    thread_2 = threading.Thread(target=main_bot_thread)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Les deux threads ont été arrêtés.")