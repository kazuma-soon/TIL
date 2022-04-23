def fiv(x)
  p 'OK'
  if x == 1 || x == 2
     1
  else
     fiv(x-2) + fiv(x-1)
  end
end

############################

a, b = 1, 1
while a < 1000
  print "#{a} "
  a, b = b, a + b
end

