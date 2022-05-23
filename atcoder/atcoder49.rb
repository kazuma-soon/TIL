n = gets.to_i
a = gets.split.map(&:to_i).sort
ans = 0
(n-1).times do |i|
  ans += a[i+1]-a[i]
end
puts ans