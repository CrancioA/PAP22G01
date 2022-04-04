"""
Create a context manager that will time how long it took to execute the context code block and display a graph with execution time when the context ends.

Since the same instance can be used in multiple contexts make sure that the graph will show data for each time the object was used in a context. See usage example below
You will need to store the graph in the context object in order to be able to update graph information on each run
In order to use the same instance and store the graph information the context object is created before we use the "with" statement
"""
from time import sleep, time
import matplotlib.pyplot as plt

class MyMyContextManager:

    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time()
        times = self.end_time-self.start_time
        print(times)
        plt.dpi = 200
        plt.plot([i for i in range(int(times+1))], label="Execution time")
        plt.legend()
        plt.xlabel('number of function calls')
        plt.ylabel('seconds')
        plt.title("My example Graph")
        plt.show()


obj = MyMyContextManager()
with obj as value1:
    sleep(1)
with obj as value2:
    sleep(2)
with obj as value3:
    sleep(3)


# Now graph will contain 3 values based on how long each context needed to execute. Notice that you will not even be
# the value1-3 objects inside the context. You can even choose to write the context as
# with obj:
# code

