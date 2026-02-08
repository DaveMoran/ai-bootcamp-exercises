from time import sleep, time
from typing import Any
import asyncio


async def greet_async(name: str, delay: float) -> str:
    """
    Wait for `delay` seconds, then return greeting.

    Args:
        name: Person to greet
        delay: Seconds to wait before greeting

    Returns:
        Greeting message with timestamp
    """
    # TODO: Implement
    sleep(delay)
    greeting = f"Hello, {name}!"
    return greeting


async def fetch_data_async(item_id: int, delay: float) -> dict:
    """
    Simulate fetching data with async delay.

    Args:
        item_id: ID of item to fetch
        delay: Simulated network latency

    Returns:
        Dictionary with item_id and timestamp
    """
    # TODO: Implement
    sleep(delay)
    data = {"item_id": item_id, "data": "Sample Data"}
    return data


async def main_sequential():
    """
    Call greet_async and fetch_data_async sequentially.
    Print total time taken.
    """
    # TODO: Implement - call functions one after another
    start_time = time()
    await greet_async("Alice", 2)
    await fetch_data_async(42, 3)
    end_time = time()

    print(f"Total time taken: {end_time - start_time} seconds")
    pass


async def main_concurrent():
    """
    Call greet_async and fetch_data_async concurrently using asyncio.gather().
    Print total time taken.
    """
    # TODO: Implement - use asyncio.gather()
    start_time = time()
    coroutines = [greet_async("Alice", 2), fetch_data_async(42, 3)]
    results = await asyncio.gather(*coroutines)
    end_time = time()

    print(f"Total time taken: {end_time - start_time} seconds")
    pass
