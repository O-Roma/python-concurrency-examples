## Multiprocessing in Python

Multiprocessing is a technique in Python that allows multiple processes to run in parallel, leveraging multiple CPU cores. Unlike threading, which suffers from the Global Interpreter Lock (GIL) and cannot achieve true parallel execution, multiprocessing creates separate processes, each with its own memory space, allowing for true parallelism. This makes it ideal for CPU-bound tasks.

### Key Concepts

- **Process**: A separate instance of a program with its own memory space, running independently.
- **Global Interpreter Lock (GIL)**: A limitation in CPython that prevents multiple threads from executing Python bytecode simultaneously. Multiprocessing bypasses this by using separate processes.
- **Inter-Process Communication (IPC)**: Since processes do not share memory, they communicate using mechanisms like Queues, Pipes, or shared memory.
- **ProcessPoolExecutor**: A high-level API from `concurrent.futures` that simplifies managing a pool of worker processes for parallel execution.

### Basic Example

The basic example demonstrates creating multiple processes to execute tasks in parallel. Each process runs independently, and the main program waits for all processes to complete using the `join()` method.

### When to Use Multiprocessing

- Use multiprocessing for **CPU-bound tasks** that require heavy computation, such as mathematical operations, data processing, and simulations.
- Avoid using multiprocessing for **I/O-bound tasks** (e.g., network requests, file operations). In such cases, threading or asyncio may be more efficient.

### Alternatives

- **Threading**: Suitable for I/O-bound tasks where operations can overlap without requiring multiple CPU cores.
- **Asyncio**: Best for highly concurrent I/O-bound tasks, such as handling thousands of network connections asynchronously.
- **ProcessPoolExecutor vs. multiprocessing.Process**: Use `ProcessPoolExecutor` for managing multiple processes efficiently, especially when dealing with a pool of worker processes.
