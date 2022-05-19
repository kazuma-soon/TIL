a, b = gets.split
case a
when 'H'
  puts 'H' if b == 'H'
  puts 'D' if b == 'D'
when 'D'
  puts 'D' if b == 'H'
  puts 'H' if b == 'D'
end