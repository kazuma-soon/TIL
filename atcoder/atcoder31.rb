s = gets.chomp
t = %w[eraser erase dreamer dream]

t.each do |t|
  s.slice!(t)
end
puts s == '' ? 'YES' : 'NO'

s = gets.strip
regex = /^(dream|dreamer|erase|eraser)+$/
puts s.match(regex) ? 'YES' : 'NO'
