N = gets.to_i
K = gets.to_i
X = gets.to_i
Y = gets.to_i

p N > K ? (K * X) + (N - K) * Y : N * X

n = gets.to_i
k = gets.to_i
x = gets.to_i
y = gets.to_i
ans = 0
1.upto(n) do |i|
  ans += x if k > 0
  ans += y if k <= 0
  k -= 1
end
 
puts ans
