n = gets.to_i
aa = gets.chomp.split.map(&:to_i)
 
ans = 10**15
[-1, 1].each do |sign|
    cum = 0
    tans = 0
    aa.each do |a|
        sign *= -1
        cum += a
        next if cum * sign > 0
        tans += (sign - cum).abs
        cum = sign
    end
    ans = [ans, tans].min
end
puts ans