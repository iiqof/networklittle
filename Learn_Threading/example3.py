# example3.py

import threading

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        for char in self.name:
            print(str(char) + '       ' + self.name[0])



#Create new threads
thread1 = myThread("Fuck you all,Fergusson was the shit, I want to go back there", 1)
thread2 = myThread("Calm you dipshit, this is not improving anithing you stupid moron", 2)

# Start new Threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exiting the Program!!!")