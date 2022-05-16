w, h, n = gets.split.map(&:to_i)

n.times do
  x, y, a = gets.split.map(&:to_i)
  case a
  when 1 then w = w - x
  when 2 then w = x
  when 3 then h = h - y
  when 4 then h = y
  end
end

p w * h