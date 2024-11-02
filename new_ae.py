import tkinter as tk
import json
from tkinter import messagebox

root = tk.Tk()
root.title("Chọn đồ uống")

drink_var=tk.StringVar(value="Cà phê") # Giá trị mặc định

#Tạo Radiobutton cho đồ uống
tk.Label(root, text="Chọn loại đồ uống:").pack()
tk.Radiobutton(root, text="Cà phê", variable=drink_var, value="Cà phê").pack()
tk.Radiobutton(root, text="Trà", variable=drink_var, value="Tra").pack()
tk.Radiobutton(root, text="Nước ngọt", variable=drink_var, value="Nước ngọt").pack()

milk_var = tk.BooleanVar()
sugar_var = tk.BooleanVar()
# Tạo Checkbutton cho các thành phần bổ sung
tk.Label(root, text="Chọn thêm:").pack()
tk.Checkbutton(root, text="Sira", variable=milk_var).pack()
tk.Checkbutton(root, text="Đường", variable=sugar_var).pack()

size_var = tk.StringVar(value="Nhỏ") # Giá trị mặc định
#Too Option Menu cho size
sizes = ["Nhỏ", "Trung bình", "Lớn"]
tk.Label(root, text="Chọn size:").pack()
size_menu= tk. OptionMenu(root, size_var, *sizes)
size_menu.pack()

result_label = tk.Label(root)

def show_selection():
    selected_drink = drink_var.get()
    selected_extras = []

    if milk_var.get():
        selected_extras.append("Siro")
    if sugar_var.get():
        selected_extras.append("Đường")
    selected_size = size_var.get()
    extras = ", ".join(selected_extras) if selected_extras else "Không có"
    result_label.config(text=f"Bạn đã chọn: {selected_drink}\nSize: {selected_size}\nThêm: {extras}")

confirm_button = tk. Button(root, text="Xác nhận", command=show_selection)
confirm_button.pack(pady=10)

# Nhân để hiển thị kết quả
result_label.pack()
root.mainloop()