s = gets.chomp.chars
ans = ''

s.each do |s|
  case s
  when '0'
    ans += '0'
  when '1'
    ans += '1'
  when 'B'
    ans.chop!
  end
end

puts ans

s = gets.chomp
ans = ''
s.length.times do |i|
  case s[i]
  when '0' then ans += '0'
  when '1' then ans += '1'
  else ans.chop!
  end
end
puts ans