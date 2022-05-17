n = gets.to_i
t = gets.split.map(&:to_i)
m = gets.to_i

m.times do
  ps, x = gets.split.map(&:to_i)
  tdup = t.dup
  tdup[ps - 1] = x
  puts tdup.sum
end

n = gets.to_i
t = gets.split.map(&:to_i)
m = gets.to_i
p = m.times.map{gets.split.map(&:to_i)}

p.each do |i|
  m_i = i[0] - 1
  l = t[m_i]
  t[m_i] = i[1]
  puts t.sum
  t[m_i] = l
end