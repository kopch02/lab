import asyncio
import os
from time import time

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    tasks = []
    tasks.append(asyncio.create_task(factorial("A", 15)))
    tasks.append(asyncio.create_task(factorial("B", 7)))
    tasks.append(asyncio.create_task(factorial("C", 4)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(f'{time() - t0} seconds')
