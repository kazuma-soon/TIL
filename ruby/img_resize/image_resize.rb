require 'RMagick'
include Magick

files = Dir.glob('paint/*.JPG')
files.each.with_index(1) do |file, i|
  img = ImageList.new(file)
  new_img = img.resize_to_fit(300, 300)
  new_img.write("./resized/new_#{i}")
end
