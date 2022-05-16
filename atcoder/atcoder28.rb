n, x = gets.split.map(&:to_i)
c = gets.split.map(&:to_i)
cnt = 0

(0..n-2).to_a.each do |i|
  until c[i-1] + c[i] <= x
    c[i] -= 1
    cnt += 1
  end
  until c[i] + c[i+1] <= x
    c[i] -= 1
    cnt += 1
  end
end

p cnt