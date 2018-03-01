import os

curPID = os.getpid()
print('Process (%s) start...' % curPID)
# Only works on Unix/Linux/Mac:
pid = os.fork()
print(pid)
if pid == 0:
    # os.fork(): 子进程永远返回0
    currentPID = os.getpid()
    parentPID = os.getppid()
    print("pid == 0 currentPID: " + str(currentPID))
    print("pid == 0 parentPID: " + str(parentPID))
    print('I am child process (%s) and my parent is %s.' % (currentPID, parentPID))
else:
    # os.fork(): 父进程返回子进程的ID
    currentPID = os.getpid()
    parentPID = pid
    print("pid != 0 currentPID: " + str(currentPID))
    print("pid != 0 parentPID: " + str(parentPID))
    print('I (%s) just created a child process (%s).' % (currentPID, parentPID))
