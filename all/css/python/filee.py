import time,os,fnmatch,gzip,bz2
def coroutine(func):
  def wrapper(*args, **kwargs):
    ret = func(*args, **kwargs)
    ret.__next__()
    return ret
  return wrapper


reader = open('trade.txt')
spliter =(i.split() for i in reader)

adder = sum((float(f[1]) * float(f[2]) for f in spliter))

print(adder)