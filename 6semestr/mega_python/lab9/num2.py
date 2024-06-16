import asyncio
import random
import requests


async def get_ip(ip_provider):
    try:
        response = requests.get(ip_provider)
        response.raise_for_status()
        return (ip_provider, response.text)
    except requests.exceptions.RequestException:
        return None


async def get_first_available_ip(ip_providers):
    tasks = [asyncio.ensure_future(get_ip(provider)) for provider in ip_providers]
    random.shuffle(tasks)
    done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        result = task.result()
        if result:
            return result

    return None


async def main():
    ip_providers = ['https://api.ipify.org', 'http://ip-api.com']
    result = await get_first_available_ip(ip_providers)
    if result:
        print(f"Ваш ip {result[1]} первым ответил: {result[0]}")
    else:
        print("ошибка")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())