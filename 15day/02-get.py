import os

pid = os.fork()
if pid < 0:
	print("fork调用失败")
elif pid == 0:
	print(
          "子进程%d PID=%d PPID=%d"
           %(pid,os.getpid(),os.getppid())
            )
else:
	print(
          "父进程%d PID=%d PPID=%d"
           %(pid,os.getpid(),os.getppid())
            )

print("执行代码为UTF-8 CVS=FISS")





