import time

def simple_timer():
    duration = int(input("Enter the timer duration in seconds: "))
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)

    print("Time's up!")

# Usage: Run the function to start the timer
simple_timer()
