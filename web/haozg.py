import time
import asyncio



async def greet(word):
    await asyncio.sleep(1)
    print("Hello,%s"%word)


async def main():
    start_time = time.time()
    await greet("Wrold!")
    await greet("China!")
    end_time = time.time()
    print(end_time-start_time)

if __name__ == "__main__":
    asyncio.run(main())



