import concurrent.futures
import time
import threading

# Define a function that will be executed in parallel
def do_work(task_id):
    thread_name = threading.current_thread().name
    print(f"Task {task_id} started with {thread_name}")
    result = task_id ** 2
    print(f"Task {task_id} completed with result: {result}")
    time.sleep(1)
    return result


def consume_messages():
    # Create a ThreadPoolExecutor with 3 worker threads

    for l in range(1,6):
        with concurrent.futures.ThreadPoolExecutor(max_workers=3,thread_name_prefix="CustomThread-") as executor:
            # Submit tasks to the executor
            task1 = executor.submit(do_work, l)

if __name__== '__main__':
    consume_messages()

