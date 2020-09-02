from os import system
for i in range(0,100000):
    command = "frida-kill " +str(i)
    print(command)
    system(command)
