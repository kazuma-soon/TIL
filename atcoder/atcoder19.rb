# n, a = gets.split.map(&:to_i)
# x = gets.split.map(&:to_i)
# cnt = 0
# (1..n).each do |n|
#   c = x.combination(n).to_a
#   c.each do |x|
#     cnt += 1 if x.sum.to_f.round(1) / n == a
#   end
# end
# p cnt

n, a = gets.to_s.split.map{|t|t.to_i}
x    = gets.to_s.split.map{|t|t.to_i - a}.sort.reverse

h = Hash.new(0)
h[0] = 1
x.each do |t|
  s = h.dup
  p s
  h.each do |(k,v)|
    next if k+t < 0
    s[k+t] += v
  end
  h = s.dup
end

puts h[0] - 1