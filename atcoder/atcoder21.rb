a = gets.chomp.chars
b = gets.chomp.chars
c = gets.chomp.chars

def turn_a(a, b, c)
  return puts 'A' if a == []
  key = a.shift
  turn_a(a, b, c) if key == 'a'
  turn_b(a, b, c) if key == 'b'
  turn_c(a, b, c) if key == 'c'
end

def turn_b(a, b, c)
  return puts 'B' if b == []
  key = b.shift
  turn_a(a, b, c) if key == 'a'
  turn_b(a, b, c) if key == 'b'
  turn_c(a, b, c) if key == 'c'
end

def turn_c(a, b, c)
  return puts 'C' if c == []
  key = c.shift
  turn_a(a, b, c) if key == 'a'
  turn_b(a, b, c) if key == 'b'
  turn_c(a, b, c) if key == 'c'
end

turn_a(a, b, c)

a = gets.chomp.chars
b = gets.chomp.chars
c = gets.chomp.chars

turn = 'a'

loop do 
  case turn
  when 'a'
    unless turn = a.shift
      puts 'A'
      exit
    end
  when 'b'
    unless turn = b.shift
      puts 'B'
      exit
    end
  when 'c'
    unless turn = c.shift
      puts 'C'
      exit
    end
  end
end