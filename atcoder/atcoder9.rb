h, w = gets.split.map(&:to_i)
r, c = gets.split.map(&:to_i)
cell = 4

cell -= 1 if r == 1
cell -= 1 if r == h
cell -= 1 if c == 1
cell -= 1 if c == w

p cell

h, w = gets.split.map(&:to_i)
r, c = gets.split.map(&:to_i)
cell = 0
(1..h).each do |i|
  (1..w).each do |j|
    if (r-i).abs + (c-j).abs == 1
      cell += 1
    end
  end
end
p cell