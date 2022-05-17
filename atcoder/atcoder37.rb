n = gets.to_i
s = gets.chomp
cnt = 0
a = []

n.times do |i|
  cnt += 1 if s[i] == 'I'
  cnt -= 1 if s[i] == 'D'
  a[i] = cnt
end

p a.max >= 0 ? a.max : 0
