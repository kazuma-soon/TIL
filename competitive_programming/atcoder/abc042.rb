puts gets.split.map(&:to_i).sort == [5, 5, 7] ? 'YES' : 'NO'

group = gets.split.map(&:to_i).group_by(&:itself)
puts group[5]&.length == 2 && group[7]&.length == 1 ? 'YES' : 'NO'

, l = gets.split.map(&:to_i)
uts n.times.map {gets.chomp}.sort.join

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

