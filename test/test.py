from threading import Timer
import time

def task(n):
	print('something...', n)
	
def test():
	Timer(10, task, (1,)).start()
	Timer(5, task, (2,)).start()

if __name__ == '__main__':
	test()
	while True:
		print(time.time())
		time.sleep(3)

