## Threading in Python

Threading is a technique in Python to run multiple operations concurrently in the same process space. It is particularly useful for I/O-bound tasks, such as reading from a file or network operations, where the program can perform other operations while waiting for the I/O operation to complete.
This is an example of concurrency in python but not parallelism. This is because of the GIL which prevents threads to execute Python bytecode in parallel, instead multiple tasks have the ability to run in overlapping time periods but aren't necessarily running at the exact same instant. Whereas with Parallelism they would literally be running at the same time on multiple processors or cores.

### Key Concepts

- **Thread**: The smallest unit of a process that can be scheduled and executed by the operating system.
- **GIL (Global Interpreter Lock)**: A mutex(a lock) that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This means that threading is not suitable for CPU-bound tasks in Python.
- **Thread Safety**: Ensuring that shared data is accessed by only one thread at a time to prevent data corruption.

### Basic Example

The basic example demonstrates creating two threads: one for printing numbers and another for printing letters. Both threads run concurrently, and the main program waits for both threads to complete using the `join()` method.

### When to Use Threading

- Use threading for I/O-bound tasks to improve performance by overlapping I/O operations with other computations.
- Avoid using threading for CPU-bound tasks due to the GIL, which can lead to performance degradation.

### Alternatives

- **Multiprocessing**: For CPU-bound tasks, consider using the `multiprocessing` module, which creates separate processes with their own Python interpreter and memory space.
- **Asyncio**: For I/O-bound tasks, especially when dealing with many connections, consider using the `asyncio` module for asynchronous programming.