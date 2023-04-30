def outer_func():
  def inner_func():
    a=9
    print("Inside inner_func, a is {:d}(id ={:d})".format(a, id(a)))
    print("inside inner_func , b is {:d}(id={:d})".format(b,id(b)))
    print("inside inner_func, len is {:d}(id={:d})".format(len, id(len))

  len=2

  print("inside outer_func, a is {:d}(id={:d})".format(a, id(a)))
  print("inside outer_func, b is {:d}(id={:d})".format(b, id(b)))
  print("inside outer_func, len is {:d}(id={:d})".format(len, id(len)))

a,b =6,7
print("in global scope, a is {:d}(id={:d})".format(a, id(a)))
print("in global scope, b is {:d}(id={:d})".format(b , id(b))
print( "In global scope, len is", len, "(id={:d})".format(id(len))
