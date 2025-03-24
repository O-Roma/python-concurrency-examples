# Basic Threading Example

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"{time.time():.4f} - {threading.current_thread().name} - Number: {i}")
        time.sleep(1)
    
def print_letters():
    for letter in 'YHWH':
        print(f"{time.time():.4f} - {threading.current_thread().name} - Letter: {letter}")
        time.sleep(1)

def print_symbols():
    for symbol in "@#$%^":
        print(f"{time.time():.4f} - {threading.current_thread().name} - Symbol: {symbol}")
        time.sleep(1)

def compute_heavy():
    for i in range(1, 6):
        print(f"{time.time():.4f} - {threading.current_thread().name} - Heavy computation {i}")
        sum(x*x for x in range(10**6))

number_thread = threading.Thread(target=print_numbers, name="NumberThread")
letter_thread = threading.Thread(target=print_letters, name="LetterThread")
symbol_thread = threading.Thread(target=print_symbols, name="SymbolThread")
cpu_thread = threading.Thread(target=compute_heavy, name="CPUThread")

#Each line runs a different target function
number_thread.start()
letter_thread.start()
symbol_thread.start()
cpu_thread.start()

#this means that the Main thread waits for each thread to complete before continuing
number_thread.join()
letter_thread.join()
symbol_thread.join()
cpu_thread.join()

print("All threads have finished execution.")


'''
python basic_thread.py
1742770907.2760 - NumberThread - Number: 1
1742770907.2790 - LetterThread - Letter: Y
1742770907.2800 - SymbolThread - Symbol: @
1742770907.2800 - CPUThread - Heavy computation 1
1742770907.3877 - CPUThread - Heavy computation 2
1742770907.4795 - CPUThread - Heavy computation 3
1742770907.5989 - CPUThread - Heavy computation 4
1742770907.7608 - CPUThread - Heavy computation 5
1742770908.2823 - SymbolThread - Symbol: #
1742770908.2840 - LetterThread - Letter: H
1742770908.2840 - NumberThread - Number: 2
1742770909.2949 - SymbolThread - Symbol: $1742770909.2949 - LetterThread - Letter: W
1742770909.2949 - NumberThread - Number: 3

1742770910.3046 - LetterThread - Letter: H
1742770910.3064 - SymbolThread - Symbol: %
1742770910.3064 - NumberThread - Number: 4
1742770911.3115 - NumberThread - Number: 51742770911.3115 - SymbolThread - Symbol: ^

All threads have finished execution.
'''