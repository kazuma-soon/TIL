n, x  = gets.split.map(&:to_i)
items = gets.split.map(&:to_i)

items.map!.with_index { |item, i| i.odd? ? item -= 1 : item }
puts x >= items.sum ? 'Yes' : 'No'