import concurrent.futures
import threading
import time

# Define a function that will be executed in parallel
def do_work(task_id):
    thread_name = threading.current_thread().name
    print(f"Task {task_id} started on thread {thread_name}")
    result = task_id ** 2
    print(f"Task {task_id} completed on thread {thread_name} with result: {result}")
    time.sleep(10)
    return result

def consume_messages():
        # Create a ThreadPoolExecutor with 3 worker threads and custom thread names
    with concurrent.futures.ThreadPoolExecutor(max_workers=6, thread_name_prefix="CustomThread-") as executor:
        thread_name = threading.current_thread().name
        for task_id in range(1, 6):
            print(f"started on thread {thread_name}")
            # Submit tasks to the executor using a for loop
            tasks = executor.submit(do_work, task_id)


if __name__== '__main__':
    consume_messages()
