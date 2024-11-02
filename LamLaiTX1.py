import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

root = tk.Tk()
root.title("Quản lý công việc cá nhân")

root.columnconfigure([0,1,2], weight=1, minsize=0)
root.rowconfigure([0,1,2,3,4], weight=1, minsize=0)

label1 = tk.Label(root, text="Tên công việc")
label1.grid(row=0, column=0, sticky="ne", pady=10, padx=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, columnspan=2, sticky="wne", pady=10, padx=10)

label2 = tk.Label(root, text="Mô tả")
label2.grid(row=1, column=0, sticky="ne", pady=10, padx=10)

text1 = tk.Text(root, height=5, width=30)
text1.grid(row=1, column=1, columnspan=2, sticky="wne", pady=10, padx=10)

lb1 = tk.Listbox(root, height=10, width=30)

with open("Tasks.json", 'r') as file:
    data = json.load(file)
    names = [i["name"] for i in data]
    descriptions = [j["description"] for j in data]
    created_ats = [k["created_at"] for k in data]

def HienThi():
    lb1.delete(0, tk.END)
    for i in range(len(data)):
        temp = data[i]
        lb1.insert(tk.END, str(temp))

HienThi()

def Them():
    name = entry1.get()
    description = text1.get("1.0", tk.END)
    created_at = datetime.now()
    data.append({"name": name, "description": description.replace("\n",""), "created_at": str(datetime.now())})
    with open("Tasks.json", 'w') as file:
        json.dump(data, file, indent=4)
    HienThi()

def HienThiLai(event):
    global index
    index = lb1.curselection()[0]
    value = lb1.get(index)
    value = value.replace("'", '"')
    value = json.loads(value)
    entry1.delete(0, "end")
    entry1.insert(0, value["name"])
    text1.delete("1.0", tk.END)
    text1.insert(tk.END, value["description"])

lb1.bind("<Double-Button>", HienThiLai)

def Sua():
    data[index] = {"name": entry1.get(), "description": text1.get("1.0", tk.END).replace("\n",""), "created_at": str(datetime.now())}
    with open("Tasks.json", 'w') as file:
        json.dump(data, file, indent=4)
        HienThi()

button1 = tk.Button(root, text="Thêm công viec", command=Them)
button1.grid(row=2, column=1, sticky="w", pady=10, padx=10)

button2 = tk.Button(root, text="Sửa công việc", command=Sua)
button2.grid(row=2, column=2, sticky="e", pady=10, padx=10)

lb1.grid(row=3, column=0, columnspan=3, sticky="wne", pady=10, padx=10)









root.mainloop()

