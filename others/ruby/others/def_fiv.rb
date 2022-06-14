def fiv(i)
  return 0 if i == 0
  return 1 if i == 1
  fiv(i-2) + fiv(i-1)
end

p fiv(10)

def fiv(i)
  return 1 if i == 0
  return 1 if i == 1
  fiv(i-2) + fiv(i-1)
end

p fiv(10)