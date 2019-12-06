# from stopwatch import Stopwatch
# stopwatch = Stopwatch()

# a = stopwatch.start()

# # if a > 10:
# # 	print("helo")
# # stopwatch.stop()
# # exit()

# n = 0
# while  True:
# 	c = 0
# 	n+=1
# 	b = str(a)
# 	c = float(b[:-2])
# 	d = c/1000
# 	# if b[-2] ==  "μ":
# 	# 	c = float(b[:-2])/1000
# 	# 	print(c)
# 	# 	pass
# 	# else:
# 	# 	c = float(b[:-2])

# 	print(d)

# 	if d > 10 μ:
# 		break
		 	


from timeutils import Stopwatch
import time

sw = Stopwatch(start=True)

x = 0
for i in range(3):
	time.sleep(1)
	print(sw.elapsed_seconds)
	# s = time.time()
	# e = time.time() - s



# sw = Stopwatch(start=True)
# time.sleep(2)
# print(sw.elapsed_seconds)
# str(sw.stop())
# print(sw.elapsed.human_str())

# for i in range(3):
# 	time.sleep(2)