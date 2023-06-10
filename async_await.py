# import asyncio
# import time

# async def worker():
#     print('worker - will take some time')
#     time.sleep(3)
#     print('worker - done it')
#     return 42

# async def do_something():
#     print('do_something - will wait for worker')
#     result = await worker()
#     print('do_something - result: ',result)

# def main():
#     print('Main - Starting')
#     asyncio.run(do_something())
#     print('Main - Done')

# if __name__ == '__main__':
#     main()

# import asyncio

# async def worker():
#     print('worker - will take some time')
#     await asyncio.sleep(1)
#     print('worker - Done it')
#     return 42

# def print_it(task):
#     print('print_it result:',task.result())

# async def do_something():
#     print('do_something - create task for worker')
#     task = asyncio.create_task(worker())
#     print('do_something - add a callback')
#     task.add_done_callback(print_it)
#     await task
#     print('do_something - task.cancelled()',task.cancelled())
#     print('do_something - task.done()',task.done())
#     print('do_something - task.result()',task.result())
#     print('do_something - task.exception()',task.exception())
#     print('do_something - finished')

# def main():
#     print('Main - Starting')
#     asyncio.run(do_something())
#     print('Main - Done')

# if __name__ == '__main__':
#     main()

# import asyncio
# import random

# async def worker():
#     print('Worker - will take some time')
#     await asyncio.sleep(1)
#     result = random.randint(1,10)
#     print('Worker - Done')
#     return result

# async def do_something():
#     print('do_something - will wait for worker')
#     # Run four workers concurrently
#     results = await asyncio.gather(
#         worker(),worker(),worker(),worker()
#     )
#     print('results from calls: ',results)

# def main():
#     print('Main - Starting')
#     asyncio.run(do_something())
#     print('Main - Done')

# if __name__ == '__main__':
#     main()


# import asyncio
# import random

# async def worker(label):
#     print('Worker - will take some time')
#     await asyncio.sleep(1)
#     result = random.randint(1,10)
#     print('Worker - Done')
#     return label + str(result)

# async def do_something():
#     print('do_something - will wait for worker')
#     # Run four calls to worker concurrently
#     for async_func in asyncio.as_completed(
#         (
#             worker('A'),worker('B'),worker('C'),worker('D')
#         )
#     ):
#         result = await async_func
#         print('do_something - result: ',result)

# def main():
#     print('Main - Starting')
#     asyncio.run(do_something())
#     print('Main - Done')

# if __name__ == '__main__':
#     main()


import asyncio
import math

async def worker(n):
    print('Worker - will take some time')
    await asyncio.sleep(0.1)
    result = math.factorial(n)
    return result

async def calculate_factorial(l):
    for async_fun in asyncio.as_completed(
        (
            worker(l[0]),worker(l[1]),worker(l[2]),worker(l[3])
        )
        ):
        result = await async_fun
        print('factorial is: ',result)

def main():
    print('Main - Starting')
    asyncio.run(calculate_factorial([5,7,3,6]))
    print('Main - Done')

if __name__ == '__main__':
    main()

