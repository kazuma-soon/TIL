n, d, h = gets.chomp.split.map(&:to_i)
min = nil
n.times{
    di, hi = gets.chomp.split.map(&:to_i)
    katamuki = (h - hi).to_f / (d - di)
    min = katamuki if min.nil? || min > katamuki
}
puts [h - min * d, 0.0].max