import subprocess
import random
class Cracking:
    def __init__(self,pass_guess):
        self.pass_guess = pass_guess
    
    def return_Guess(self):
        return self.pass_guess

    def Crack_pass(self):
        guess = self.pass_guess.encode('utf-8')
        result = subprocess.run(["java", "Password_2"], input= guess , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip()

Letters = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a",]
Attempts =[]
while(True):
    guess = ''.join(random.sample(Letters,2))
    if guess in Attempts:
        pass
    else:
        Attempts.append(guess)
        print(guess)
        Guessing = Cracking(guess)
        if(Guessing.Crack_pass().find("Agian")==-1):
            print("we did it the password is: ",Guessing.return_Guess())
            break
