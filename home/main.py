import threading

def calculate_sum(part, result, index):
    result[index] = sum(part)

def main():
    numbers = list(range(1, 1001))
    half = len(numbers) // 2
    part1, part2 = numbers[:half], numbers[half:]
    result = [0, 0]

    thread1 = threading.Thread(target=calculate_sum, args=(part1, result, 0))
    thread2 = threading.Thread(target=calculate_sum, args=(part2, result, 1))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    total_sum = sum(result)
    print("Umumiy yig'indi:", total_sum)

main()


