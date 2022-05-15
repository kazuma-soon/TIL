n = gets.to_f
a = gets.split.map(&:to_i)
avg = (a.sum / n).round
cst = 0
a.each do |a|
  cst += (a - avg).abs ** 2
end
p cst