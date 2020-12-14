import subprocess
import time

def cmdAgain():
	global p
	cmd = ["nc", "-ul", "9"]
	p = subprocess.Popen(cmd,
						stdout=subprocess.PIPE,
						stderr=subprocess.STDOUT)
cmdAgain()
while (1):
	if p.stdout.read(1) == b'\x82':
		print("stop")
		p.kill()
		time.sleep (1)
		cmdAgain()




