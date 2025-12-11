import requests
import time
import concurrent.futures

URL = "http://44.201.248.175:5000/api/users/"

# Кількість паралельних потоків
THREADS = 50

# Кількість запитів на кожен потік
REQUESTS_PER_THREAD = 200


def spam():
    for _ in range(REQUESTS_PER_THREAD):
        try:
            r = requests.get(URL, timeout=2)
            print(f"{r.status_code} - {r.text[:50]}")
        except Exception as e:
            print("Error:", e)
        time.sleep(0.01)


def main():
    print("🚀 Starting load test...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(lambda _: spam(), range(THREADS))

    print("✅ Load test finished.")


if __name__ == "__main__":
    main()
