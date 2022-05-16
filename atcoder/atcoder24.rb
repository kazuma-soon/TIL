array = gets.split.map(&:to_i)
puts array.min(2).sum == array.max ? 'Yes' : 'No'