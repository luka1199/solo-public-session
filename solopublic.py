import psutil
import time

TARGET = "GTA5.exe"

def main():
    for proc in psutil.process_iter():
        if proc.name() == TARGET:
            starttime = time.time()
            proc.suspend()
            while (time.time() - starttime) < 9:
                pass
            proc.resume()

if __name__ == '__main__':
    main()
