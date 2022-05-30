n, m = gets.split.map(&:to_i)
sc = m.times.map{gets.split.map(&:to_i)}
(0..999).each do |i|
  cnt = 0
  i = i.to_s
  sc.each do |j|
    cnt += 1 if i[j[0]-1] == j[1].to_s
  end
  if cnt == m
    if i.to_i.digits.count == n
      puts i
      exit
    end
  end
end
puts -1