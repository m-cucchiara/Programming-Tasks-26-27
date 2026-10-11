"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
from collections import deque
import time

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.

    speedOfQueue = int(input("Enter the how fast the queue should be (lowest number makes queue faster, highest makes queue slower): "))

    i = 0
    queue = deque()

    while i != 100:

        if i % speedOfQueue == 0 and len(queue) != 0:
            queue.popleft()
        else:
            queue.append("Customer " + str(i))

        if len(queue) != 0:
                    i = i + 1

        time.sleep(1)

        print("Length of queue: ", len(queue))
        print("Last customer has tag number", i)

    print("Shop is closed! come back another day!")





if __name__ == "__main__":
    main()
