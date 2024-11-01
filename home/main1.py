import threading

def convert_to_uppercase(text, result, index):
    result[index] = text.upper()

def main():
    messages = ["hello", "world", "threading", "is", "fun"]
    result = [None] * len(messages)

    threads = []
    i = 0
    while i < len(messages):
        thread = threading.Thread(target=convert_to_uppercase, args=(messages[i], result, i))
        threads.append(thread)
        thread.start()
        i += 1

    j = 0
    while j < len(threads):
        threads[j].join()
        j += 1

    print("Katta harflardagi xabarlar:", result)

main()
