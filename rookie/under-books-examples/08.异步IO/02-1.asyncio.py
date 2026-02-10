"""
    大致看了下 @asyncio.coroutine + get_event_loop(), 可以大概理解
    当然, 还是async await比较香

"""

import asyncio
import threading

async def hello(name):
    print("Hello %s! (%s)" % (name, threading.current_thread))
    await asyncio.sleep(5)
    print("Hello %s again! (%s)" % (name, threading.current_thread))
    return name

async def he():
    await hello("Alice")

async def main():
    L = await asyncio.gather(hello("Bob"), hello("Alice"))
    print(L)

if __name__ == '__main__':
    asyncio.run(he())
    asyncio.run(main())