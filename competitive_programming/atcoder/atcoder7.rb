array = gets.chomp.split(' ').group_by(&:itself).map{|k, v| [k, v.size]}
puts "#{array.max_by{ |x| x[1] }[0]} #{array.max_by{ |x| x[0].length }[0]}"

array = gets.split.group_by(&:itself)
puts array.max_by{ |k,v| v.length }[0] + " " + array.max_by{ |k, v| k.length }[0]

