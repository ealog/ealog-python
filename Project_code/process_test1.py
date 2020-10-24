import time
import multiprocessing

def work():
    for i in range(10):
        print("working....",i)
        time.sleep(0.5)


def main():
    work_process = multiprocessing.Process(target=work)
    work_process.daemon = True
    work_process.start()
    # work_process.join()

    time.sleep(1)
    print("Job done.")


if __name__ == "__main__":
    main()