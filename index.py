from multiprocessing import Pool
import time


def cube(x):
	time.sleep(3)
	return x**3

def pool_handle():
	p=Pool(3)
	kq=p.map_async(cube, [1,2,3])
	print("ahudeptrai")
	print(kq.get())

if __name__ == "__main__":
	pool_handle()