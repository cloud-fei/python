from asyncio import subprocess
import os
import subprocess


'''
os.system(command)                 返回命令执行状态码，并将命令执行结果输出到屏幕
os.popen(command).read()           可以获取命令执行结果，但是无法获取命令执行状态码
commands.getstatusoutput(command)  返回一个元组(命令执行状态码, 命令执行结果)   只有linux能够使用
'''


shell_command = " ostname"
ret1 = os.system(shell_command)
#ret2 = os.popen(shell_command).read()

print(ret1)        #node1 0                
#print(ret2)        #node1


'''
subprocess模块  本质是通过popen实现
before 3.5   subprocess.call()，   subprocess.getoutput() ---不打印在屏幕上
after 3.5    subprocess.run()
'''

#subprocess.run("hostname")    #node1

#subprocess.call("hostname")    #node1

#ret = subprocess.getoutput("hostname")  #node1
#print(ret)




