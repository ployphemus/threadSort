import threading
import time


def sort_by_thread_wait_time(array):
    """Sorts an array of ints by assigning the values as thread wait times and storing them back to a new array in the order that the threads finish.

    Args:
      array: A list of ints.

    Returns:
      A new list of ints sorted in the order that the threads finish.
    """

    # Create a new list to store the sorted results.
    sorted_array = []

    # Create a list of threads.
    threads = []
    for i in range(len(array)):
        thread = threading.Thread(target=_sort_by_thread_wait_time_helper, args=(array[i], sorted_array))
        threads.append(thread)

    # Start all of the threads.
    for thread in threads:
        thread.start()

    # Wait for all of the threads to finish.
    for thread in threads:
        thread.join()

    # Return the sorted array.
    return sorted_array


def _sort_by_thread_wait_time_helper(wait_time, sorted_array):
    """Helper function for sort_by_thread_wait_time.

    Args:
      wait_time: The amount of time to wait.
      sorted_array: The list to store the sorted results in.
    """

    time.sleep(wait_time)
    sorted_array.append(wait_time)


array = [1, 44, 2, 88, 15, 25, 30, 20, 9, 10]

sorted_array = sort_by_thread_wait_time(array)

print(sorted_array)
