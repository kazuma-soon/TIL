N = gets.to_i
i = 1
k = 1
while i < N
  k *= i+1
  k %= 10**9 + 7
  i += 1
end
puts k
