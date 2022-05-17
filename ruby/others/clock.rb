# ライブラリなしで時計を作成する
# 実行すると、00:00:01ってはじまるイメージ

60.times { |h|  
  60.times { |m|
    60.times { |s|
      printf("%02d:", "#{h}")  # hour
      printf("%02d:", "#{m}")  # minute
      printf("%02d\n", "#{s}") # second
      sleep 1
    }
  }
}