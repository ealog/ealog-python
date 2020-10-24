import time
import threading

def work():
    for i in range(10):
        print("working...")
        time.sleep(0.2)

def main():
    work_thread = threading.Thread(target=work)
    work_thread.setDaemon(True)
    work_thread.start()
    time.sleep(1)
    print("job done...")

if __name__ == "__main__":
    main()