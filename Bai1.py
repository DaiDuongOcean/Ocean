import json

# Chuỗi JSON
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Chuyển đổi chuỗi JSON sang từ điển
data_dict = json.loads(json_string)

# Kiểm tra kết quả
print(data_dict)
print(data_dict["name"])  # In ra giá trị của khóa "name"