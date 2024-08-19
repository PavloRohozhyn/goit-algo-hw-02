from queue import Queue
import random

def generate_request(queue):
    """ creator """
    # Створити нову заявку
    task = random.randint(0, 1000)
    # Додати заявку до черги
    queue.put(task)
    print('Task added in to queue')
    print(queue.queue)
    return queue

def process_request(queue):
    """ processor """
    # Якщо черга не пуста:
    if not queue.empty():
        # Видалити заявку з черги
        data = queue.get()
        # Обробити заявку
        print(f'The task {data} already processed')
        print(queue.queue)
    # Інакше:
    else:
        # Вивести повідомлення, що черга пуста
        print ('The queue is empty')

def main():
    """ Main funciton """

    # Створити чергу заявок
    queue = Queue()

    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Show tasks in to queue")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            generate_request(queue)
        elif choice == '2':
            process_request(queue)
        elif choice == '3':
            queue = None
            print("Stop...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2 or 3.")

if __name__ == "__main__":
    main()
