import client
import time
import traceback

while True:
	try:
		client.debugHandleLine()
	except:
		traceback.print_exc()
		time.sleep(2)
		continue
	time.sleep(30)

