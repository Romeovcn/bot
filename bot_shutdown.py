import os
import time

def shutdown():
    os.system("shutdown /s /f /t 0")

if __name__ == "__main__":
    time.sleep(2)
    shutdown()