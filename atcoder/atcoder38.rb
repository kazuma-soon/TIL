n = gets.to_i
f = (1..n).inject(:*)
def divisor(num)
  (1..num).select{ |i| num % i == 0 }
end

p divisor(f).count % (10**9 + 7)