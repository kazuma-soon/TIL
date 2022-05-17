n, m = gets.split.map(&:to_i)
a = []
b = []
n.times do
  a << gets.chomp
end
m.times do
  b << gets.chomp
end
p a, b