a, b = gets.split.map(&:to_i)
c = b - a

p ( (1..c).inject(:+) - b ).abs