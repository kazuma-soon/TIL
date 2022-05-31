n = gets.to_i
p = gets.split.map(&:to_i)
min = 10 ** 9
cnt = 0
p.each do |i|
  if i < min
    cnt += 1
    min = i
  end
end
puts cnt