p=0
def nested_sum(t):
  global p
  for x in t:
    if isinstance(x,list):
      nested_sum(x)
    else:
       p+=x
  return p
total=[25,10,[5,6],5]
d=nested_sum(total)
print(d)

  
