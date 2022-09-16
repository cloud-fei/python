import os

shell_command = " hostname"
ret = os.popen(shell_command)
data = ret.read()
print(data)

