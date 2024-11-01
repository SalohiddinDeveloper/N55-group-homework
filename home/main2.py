import threading

def double_number(number, result, index):
    result[index] = number * 2

def main():
    user_input = input("Raqamlarni kiriting (bo'sh joy bilan ajratilgan): ")
    input_list = user_input.split()
    numbers = []
    i = 0
    while i < len(input_list):
        numbers.append(int(input_list[i]))
        i += 1

    result = [None] * len(numbers)
    threads = []

    i = 0
    while i < len(numbers):
        thread = threading.Thread(target=double_number, args=(numbers[i], result, i))
        threads.append(thread)
        thread.start()
        i += 1

    i = 0
    while i < len(threads):
        threads[i].join()
        i += 1

    i = 0
    while i < len(result):
        print(result[i])
        i += 1

main()
