# gets
# a = gets.split.map(&:to_i).sort
# b = (0..a.last).to_a
# 
# p (b - a).min
# 

# O(N)
N = gets.to_i
arr = gets.chomp.split(" ").map(&:to_i)
max = arr.max
hash = {}
arr.each do |num|
  hash[num] = true
end

i = 0
while i <= max
  break if hash[i] != true
  i += 1
end
puts i