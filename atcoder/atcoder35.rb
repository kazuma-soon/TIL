k, s = gets.split.map(&:to_i)
cnt = 0
(0..k).each do |x|
  (0..k).each do |y|
    z = s - x - y
    cnt += 1 if 0 <= z && z <= k
  end
end
p cnt