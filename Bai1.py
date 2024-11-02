import tkinter as tk
import json
from tkinter import messagebox

class UserManage:
    def __init__(self):
        self.loadusers()

    def loadusers(self):
        with open("users.json", 'r') as file:
            data = json.load(file)
            self.users = data['users']
            self.usernames = [i['username'] for i in self.users]
            self.passwords = [j['password'] for j in self.users]

    def saveusers(self):
        with open("users.json", 'w') as file:
            json.dump({"users": self.users}, file, indent=4)

    def check_login(self, username, password):
        for i in range(len(self.usernames)):
            if username == self.usernames[i] and password == self.passwords[i]:
                return True
        return False

    def register_user(self, username, password):
        if username in self.usernames:
            return False

        def check(string):
            c1 = string.isalnum()
            return c1

        if check(username) and check(password):
            self.users.append({"username": username, "password": password})
            self.saveusers()
            self.loadusers()
            return True

        return False

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.columnconfigure([0, 1], weight=1, minsize=50)
        self.root.rowconfigure([0, 1, 2], weight=1, minsize=50)
        self.usermanage = UserManage()

        self.label1 = tk.Label(self.root, text="Username")
        self.entry1 = tk.Entry(self.root)
        self.label2 = tk.Label(self.root, text="Password")
        self.entry2 = tk.Entry(self.root)

        def login():
            username = self.entry1.get()
            password = self.entry2.get()
            if self.usermanage.check_login(username, password):
                messagebox.showinfo("Thông báo", "Đăng nhập thành công")
                self.root.withdraw()
                window = tk.Toplevel()
                window.columnconfigure([0, 1], weight=1, minsize=50)
                window.rowconfigure([0, 1, 2, 3], weight=1, minsize=50)

                label1 = tk.Label(window, text="Địa chỉ IP")
                label2 = tk.Label(window, text="Cổng")
                label3 = tk.Label(window, text="Loại server")
                
                entry1 = tk.Entry(window)
                entry2 = tk.Entry(window)
                entry3 = tk.Entry(window)

                def luu():
                    with open("cauhinh.json", 'w') as file:
                        json.dump({"ip": entry1.get(), "port": entry2.get(), "type": entry3.get()}, file, indent=4)
                    messagebox.showinfo("Thông báo", "Lưu cấu hình thành công")

                def logout():
                    self.entry1.delete(0, "end")
                    self.entry2.delete(0, "end")
                    window.destroy()
                    self.root.deiconify()

                button1 = tk.Button(window, text="Lưu cấu hình", command=luu)
                button2 = tk.Button(window, text="Đăng xuất", command=logout)

                label1.grid(row=0, column=0)
                label2.grid(row=1, column=0)
                label3.grid(row=2, column=0)

                entry1.grid(row=0, column=1)
                entry2.grid(row=1, column=1)
                entry3.grid(row=2, column=1)

                button1.grid(row=3, column=0)
                button2.grid(row=3, column=1)
            else:
                messagebox.showinfo("Thông báo", "Đăng nhập không thành công")

        def signup():
            username = self.entry1.get()
            password = self.entry2.get()
            if self.usermanage.register_user(username, password):
                messagebox.showinfo("Thông báo", "Đăng ký thành công")
            else:
                messagebox.showinfo("Thông báo", "Đăng ký không thành công")

        self.button1 = tk.Button(self.root, text="Đăng nhập", command=login)
        self.button2 = tk.Button(self.root, text="Đăng ký", command=signup)

        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        self.button1.grid(row=2, column=0)
        self.button2.grid(row=2, column=1)

root = tk.Tk()
app = LoginApp(root)
root.mainloop()