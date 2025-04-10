# asyncio Examples

This folder contains examples that showcase Python's **asyncio** module for asynchronous programming. The examples provided in this section demonstrate how to run tasks concurrently by leveraging the async/await syntax along with scheduling coroutines using `asyncio.gather`.

## Examples

### 1. `basic_async.py`
- **Description:**  
  This simple script defines two asynchronous tasks that wait for a specified delay before printing a message. The tasks are executed concurrently using `asyncio.gather`.
- **Concepts Illustrated:**  
  - Basic asynchronous function definition using `async def`
  - Scheduling and running concurrent tasks using `asyncio.gather`
  - Non-blocking sleep using `asyncio.sleep`

### 2. `aiohttp_example.py`
- **Description:**  
  This script demonstrates making concurrent HTTP requests using the `aiohttp` library. It sets up a client session to send multiple asynchronous GET requests and prints a snippet of each response.
- **Concepts Illustrated:**  
  - Using `aiohttp.ClientSession` for non-blocking HTTP calls
  - Creating asynchronous fetch functions for network I/O
  - Executing multiple asynchronous HTTP requests concurrently via `asyncio.gather`

## Concurrency vs. Parallelism

- **Concurrency:**  
  The examples shown here are **concurrent**. They allow multiple tasks (e.g., network I/O operations or timed delays) to be in progress at the same time without using multiple CPU cores. Concurrency in asyncio is achieved via cooperative multitasking on a single thread using an event loop.
  
- **Parallelism:**  
  In contrast, **parallelism** involves executing multiple tasks simultaneously on different processors or cores. This usually requires multiple threads or processes. The asyncio examples here do not perform parallel execution—they simply manage tasks concurrently within one process.

---

Use these examples as a starting point for practicing asynchronous programming in Python. For more complex scenarios or to compare concurrency with threading or multiprocessing, see the additional examples provided in other parts of the repository.
