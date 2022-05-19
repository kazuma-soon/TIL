w, a, b = gets.split.map(&:to_i)
if    b > a + w
  p b - (a + w)
elsif b < a - w
  p a - (b + w)
elsif a + w <= b || a - w <= b
  p 0
end