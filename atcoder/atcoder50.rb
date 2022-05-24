h, w = gets.split.map(&:to_i)
ary = Array.new(h+2){ Array.new(w+2, '#') }
(h+2).times do |i|
  ary[i+1][1..w] = gets.chomp.chars if i < h
  puts ary[i].join
end