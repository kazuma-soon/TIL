# puts gets.split.map(&:to_i).sum < 22 ? 'win': 'bust'

puts gets.chomp.split(' ').map(&:to_i)
     .inject{|res, answer| 
        p res, answer
        res + answer}<22? :win : :bust