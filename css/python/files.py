def coroutine(func):
  def wrapper(*args, **kwargs):
    ret = func(*args, **kwargs)
    ret.__next__()
    return ret
  return wrapper

@coroutine
def writer():
  print('i am here to add stuff!')
  word = ''
  while True:
    w = yield word 
    print(word)
    word += w
    
class Logs_s:
  def __init__(self,name): 
    self.name = name 
  
  @coroutine   
  def geen(self,file):
    self.name = writer()
    with open(file) as f:
      s = (x.rsplit(None,1)[1] for x in f)
      for i in s:
        print(i)
        if i != '-': yield self.name.send(i)
    
    

dor = Logs_s('lond')
dor.geen('logs.txt')



class kiy:
  def __init__(self,name,age,sex):
    self.__name = name
    self.age = age
    self.sex = sex   
    
  @property
  def name (self):
    return self.__name
  
jud = kiy('will', 12,'male')

jud.name = 'jgtdjjy'
print(jud.name)