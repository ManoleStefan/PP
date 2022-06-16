import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=10)
loop = asyncio.get_event_loop()


def functie_calcul_inmultire(dictionar, const):
    for i in dictionar:
        dictionar[i] = dictionar[i] * const
    return dictionar


def functie_replace(dictionar):
    for i in dictionar:
        if dictionar[i] % 2 == 0:
            dictionar[i] = 0
    return dictionar


def functie_calcul_adunare(dictionar):
    for i in range(0, len(dictionar), 2):
        dictionar[i] = dictionar[i] + dictionar[i + 1]
    return dictionar


async def process_pipeline(data):
    results = await level_a(data)
    return results


async def level_a(data):
    results = await asyncio.gather(*[level_b(data)])
    result = await loop.run_in_executor(executor, functie_replace, *results)
    return result


async def level_b(data):
    results = await asyncio.gather(*[level_c(data)])
    result = await loop.run_in_executor(executor, functie_calcul_adunare, *results)
    return result


async def level_c(data):
    result = await loop.run_in_executor(executor, functie_calcul_inmultire, data, 3)
    return result


def main():
    dictionar = {
        0: 34,
        1: 12,
        2: 9,
        3: 12,
        4: 18,
        5: 21
    }
    result = loop.run_until_complete(process_pipeline(dictionar))
    print(result)


if __name__ == '__main__':
    main()
