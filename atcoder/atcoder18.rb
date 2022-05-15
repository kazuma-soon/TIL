w = gets.chomp.chars.group_by(&:itself).map {|k, v| [k, v.size]}
puts w.all? { |i| i[1] % 2 == 0 } ? 'Yes' : 'No'

w1 = gets.chomp.chars
w2 = w1.uniq
boolean = true
w2.each do |w|
  boolean = false if w1.count(w) % 2 != 0
end
puts boolean ? 'Yes' : 'No'
