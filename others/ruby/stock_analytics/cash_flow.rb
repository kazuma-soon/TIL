puts '初期投資額（万円）を入力してください。'
init = gets.to_f
puts '投資期間（年）を入力してください。'
periods = (0..gets.to_f).to_a
puts '毎年の投資額（万円）を入力してください。'
invest = gets.to_f
puts '期待する年利（%）を入力してください。（2~5% なら 2 5 と入力）'
interest = gets.split.map(&:to_f).map {|i| i / 100}

periods.each do |period|
  puts (init * 10000).round(3)
  init *= (1 + interest.sample)

  init += invest
end
