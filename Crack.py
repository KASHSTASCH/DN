import threading
import subprocess
import random
from stopwatch import Stopwatch
global counter
counter = 0
class Cracking:
    def __init__(self,pass_guess):
        self.pass_guess = pass_guess
    
    def return_Guess(self):
        return self.pass_guess

    def Crack_pass(self,fileType,fileName):
        guess = self.pass_guess.encode('utf-8')
        result = subprocess.run([fileType, fileName], input= guess , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip()
def Fistin(beg,end):
    global counter
    for i in range(beg,end):
        counter+=1
        if stop_event.is_set():
            return
        guess = ''.join(random.sample(Letters,int(numChars)))
        if guess not in Attempts:
            Attempts.add(guess)
            #print(guess)
            Guessing = Cracking(guess)
            if(Guessing.Crack_pass(fileType,fileName).find("Incorrect")==-1):
                stop_event.set()
                print("we did it the password is: ",Guessing.return_Guess())
                return

Letters = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a",]
Attempts = set()
threads = []
stop_event = threading.Event()
fileType = input("Enter your file type: ")
fileName = input("Enter your file name: ")
numChars = input("Enter the number of letters: ")
numThreads = input("Enter how many Threads you want(not to high): ")
stopwatch = Stopwatch(10)
for i in range(int(numThreads)):
    beg = (i*(len(Letters)**int(numChars)))
    end = ((i+1)*(len(Letters)**int(numChars)))
    t = threading.Thread(target = Fistin, args = (beg,end))
    threads.append(t)
    t.start()
print(str(stopwatch))
#stopwatch.stop()
for t in threads:
    t.join()
stopwatch.stop()

print(str(stopwatch))

print(Attempts)
print("PLease dont be to much ",len(Attempts))
if "ms" in str(stopwatch):
    print(float(str(stopwatch)[:-2])/(counter*100)," length in seconds per process")
elif "μs" in str(stopwatch):
    print(float(str(stopwatch)[:-2])/(counter*1000000)," length in seconds per process")
elif "s" in str(stopwatch):
    print(float(str(stopwatch)[:-1])/counter," length in seconds per process")
