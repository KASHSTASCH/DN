from subprocess import call
def Crack_pass():
    return(call(["java","Password_2"],capture_output = True))

Pass = Crack_pass()
print(Pass)
