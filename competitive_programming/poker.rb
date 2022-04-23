a, b = gets.split.map(&:to_i)
poker = [2,3,4,5,6,7,8,9,10,11,12,13,1]

if a == b
  puts 'Draw'
elsif poker.index(a) > poker.index(b)
  puts 'Alice'
else
  puts 'Bob'
end
