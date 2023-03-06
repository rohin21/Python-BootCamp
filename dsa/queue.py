class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print("Added a new element to the queue : {}".format(item))

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return "Queue Size : {}".format(len(self.queue))

    def display(self):
        print(self.queue)

