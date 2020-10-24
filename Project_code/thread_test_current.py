import threading
import time
def task():
    time.sleep(1)
    cur_thread = threading.current_thread()
    print(cur_thread)


def main():
    for i in range(10):
        task_thread = threading.Thread(target=task)
        task_thread.start()    


if __name__ == "__main__":
    main()