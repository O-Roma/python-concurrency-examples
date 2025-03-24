import multiprocessing
import time
import os

def print_numbers():
    for i in range(1, 6):
        print(f"{time.time():.4f} - PID {os.getpid()} - Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'YHWH':
        print(f"{time.time():.4f} - PID {os.getpid()} - Letter: {letter}")
        time.sleep(1)

def print_symbols():
    for symbol in "@#$%^":
        print(f"{time.time():.4f} - PID {os.getpid()} - Symbol: {symbol}")
        time.sleep(1)

def compute_heavy():
    for i in range(1, 6):
        print(f"{time.time():.4f} - PID {os.getpid()} - Heavy computation {i}")
        sum(x*x for x in range(10**6))

if __name__ == "__main__":
    number_process = multiprocessing.Process(target=print_numbers, name="NumberProcess")
    letter_process = multiprocessing.Process(target=print_letters, name="LetterProcess")
    symbol_process = multiprocessing.Process(target=print_symbols, name="SymbolProcess")
    cpu_process = multiprocessing.Process(target=compute_heavy, name="CPUProcess")

    # Start processes
    number_process.start()
    letter_process.start()
    symbol_process.start()
    cpu_process.start()

    # Wait for all processes to finish
    number_process.join()
    letter_process.join()
    symbol_process.join()
    cpu_process.join()

    print("All processes have finished execution.")

'''
python basic_process.py
1742776921.2446 - PID 15969 - Number: 1
1742776921.2494 - PID 15971 - Symbol: @
1742776921.2497 - PID 15970 - Letter: Y
1742776921.2552 - PID 15972 - Heavy computation 1
1742776921.3174 - PID 15972 - Heavy computation 2
1742776921.3750 - PID 15972 - Heavy computation 3
1742776921.4293 - PID 15972 - Heavy computation 4
1742776921.4876 - PID 15972 - Heavy computation 5
1742776922.3138 - PID 15969 - Number: 2
1742776922.5653 - PID 15971 - Symbol: #
1742776922.7040 - PID 15970 - Letter: H
1742776923.3739 - PID 15969 - Number: 3
1742776923.6251 - PID 15971 - Symbol: $
1742776923.7638 - PID 15970 - Letter: W
1742776924.6845 - PID 15971 - Symbol: %
1742776924.8238 - PID 15970 - Letter: H
1742776924.9022 - PID 15969 - Number: 4
1742776925.7443 - PID 15971 - Symbol: ^
1742776926.4304 - PID 15969 - Number: 5
All processes have finished execution.
'''