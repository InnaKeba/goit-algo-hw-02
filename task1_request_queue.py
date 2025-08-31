from queue import Queue
import time
import random

request_queue = Queue()
request_id = 1 

# Функція для генерації заявок
def generate_request():
    global request_id
    request_data = f"Request #{request_id}"
    request_queue.put(request_data)
    print(f"[+] Заявку створено та додано до черги: {request_data}")
    request_id += 1

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"[-] Обробка заявки: {current_request}")
        time.sleep(1)  
    else:
        print("[!] Черга пуста. Немає заявок для обробки.")

# Основний цикл для генерації та обробки заявок
def main():
    try:
        while True:
            if random.choice([True, False]):
                generate_request()
            process_request()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[✓] Програма завершена користувачем.")

if __name__ == "__main__":
    main()
# зупинка програми через Ctrl+C