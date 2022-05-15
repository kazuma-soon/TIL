n, k = gets.split.map(&:to_i)
d = gets.chomp.split
 
(n.to_s..'100000').each do |i|
  flag = true
  d.each do |j|
    flag = false if i.include?(j)
  end
  if flag
    return puts i
  end
end

