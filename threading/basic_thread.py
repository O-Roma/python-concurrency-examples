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


'''python basic_thread.py
1742761829.7210 - NumberThread - Number: 1
1742761829.7212 - LetterThread - Letter: Y
1742761829.7216 - SymbolThread - Symbol: @
1742761829.7217 - CPUThread - Heavy computation 1
1742761829.7808 - CPUThread - Heavy computation 2
1742761829.8504 - CPUThread - Heavy computation 3
1742761829.9310 - CPUThread - Heavy computation 4
1742761830.0055 - CPUThread - Heavy computation 5
1742761830.9481 - LetterThread - Letter: H
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761829.7210 - NumberThread - Number: 1
1742761829.7212 - LetterThread - Letter: Y
1742761829.7216 - SymbolThread - Symbol: @
1742761829.7217 - CPUThread - Heavy computation 1
1742761829.7808 - CPUThread - Heavy computation 2
1742761829.8504 - CPUThread - Heavy computation 3
1742761829.9310 - CPUThread - Heavy computation 4
1742761830.0055 - CPUThread - Heavy computation 5
1742761830.9481 - LetterThread - Letter: H
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761829.7212 - LetterThread - Letter: Y
1742761829.7216 - SymbolThread - Symbol: @
1742761829.7217 - CPUThread - Heavy computation 1
1742761829.7808 - CPUThread - Heavy computation 2
1742761829.8504 - CPUThread - Heavy computation 3
1742761829.9310 - CPUThread - Heavy computation 4
1742761830.0055 - CPUThread - Heavy computation 5
1742761830.9481 - LetterThread - Letter: H
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761829.7808 - CPUThread - Heavy computation 2
1742761829.8504 - CPUThread - Heavy computation 3
1742761829.9310 - CPUThread - Heavy computation 4
1742761830.0055 - CPUThread - Heavy computation 5
1742761830.9481 - LetterThread - Letter: H
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761829.8504 - CPUThread - Heavy computation 3
1742761829.9310 - CPUThread - Heavy computation 4
1742761830.0055 - CPUThread - Heavy computation 5
1742761830.9481 - LetterThread - Letter: H
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761829.9310 - CPUThread - Heavy computation 4
1742761830.0055 - CPUThread - Heavy computation 5
1742761830.9481 - LetterThread - Letter: H
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761830.0055 - CPUThread - Heavy computation 5
1742761830.9481 - LetterThread - Letter: H
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761830.9481 - LetterThread - Letter: H
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761831.0234 - NumberThread - Number: 2
1742761831.0234 - SymbolThread - Symbol: #
1742761832.1983 - NumberThread - Number: 3
1742761832.1983 - NumberThread - Number: 3
1742761832.1985 - SymbolThread - Symbol: $
1742761832.2506 - LetterThread - Letter: W
1742761833.3984 - NumberThread - Number: 4
1742761833.3985 - SymbolThread - Symbol: %
1742761833.5532 - LetterThread - Letter: H
1742761834.5184 - NumberThread - Number: 5
1742761834.7012 - SymbolThread - Symbol: ^
All threads have finished execution.
'''