# Thân Thị Mỹ Huyền - 20206288
# Nhập được đầu vào/đầu ra: 
# file->file:Đọc được 1 file ảnh và hiển thị chấm ra màn hình/file text


import ascii_magic
output = ascii_magic.from_image_file('C:/Users/HAN NGA/Downloads/Quotes/hồng.jpg', columns=100, char='.')
ascii_magic.to_terminal(output)