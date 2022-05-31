n = gets.to_i
s = n.times.map{gets.chomp.chars.sort}
h = s.map(&:join).tally
sum = 0
h.each do |_, v|
  sum += v*(v-1) / 2
end
puts sum