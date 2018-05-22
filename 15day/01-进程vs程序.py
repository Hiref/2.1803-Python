import os

pid = os.fork()

if pid == 0:
	print(
          "PID=1102%d"%pid
            )
else:
	print(
          "PID=ELSE%d"%pid
            )







