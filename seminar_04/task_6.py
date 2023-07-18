import asyncio
from pathlib import Path


async def counter(name):
    with open(name, 'r', encoding='UTF-8') as file:
        content = file.read()
        count = len(content.split())
        print(f'{name} count = {count}')


if __name__ == '__main__':
    tasks = []

    for file in Path('.').iterdir():
        if file.is_file():
            task = asyncio.ensure_future(counter(file))
            tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
