a, b = gets.split.map(&:to_i)
if a == b
  puts 'Draw'
elsif a == 1
  puts 'Alice'
elsif b == 1
  puts 'Bob'
elsif a > b
  puts 'Alice'
elsif b > a
  puts 'Bob'
end

A, B = gets.split.map(&:to_i)
a = (A - 2) % 13
b = (B - 2) % 13
p a, b
if a > b
  puts "Alice"
elsif a < b
  puts "Bob"
else
  puts "Draw"
end