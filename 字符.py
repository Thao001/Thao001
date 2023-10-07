import tkinter as tk
from SDES import SDES


class StringGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("字符串加密解密")
        self.root.geometry("600x400")
        self.sdes = SDES()

        self.initUI()

    def initUI(self):
        font = ("宋体", 14)

        self.inputKey = tk.Entry(self.root, font=font, width=20)
        self.inputMingAsc = tk.Entry(self.root, font=font, width=20)
        self.inputMiAsc = tk.Entry(self.root, font=font, width=20)

        self.buttonEncryptAsc = tk.Button(self.root, text="加密", font=font, command=self.encrypt_asc, bg="green", fg="white")
        self.buttonDecryptAsc = tk.Button(self.root, text="解密", font=font, command=self.decrypt_asc, bg="green", fg="white")

        self.label1 = tk.Label(self.root, text="请输入十位的密钥:", font=font)
        self.label2 = tk.Label(self.root, text="请输入明文字符串:", font=font)
        self.label3 = tk.Label(self.root, text="请输入密文字符串:", font=font)
        self.label4 = tk.Label(self.root, text="", font=font)
        self.label5 = tk.Label(self.root, text="", font=font)

        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.inputKey.grid(row=0, column=1, padx=10, pady=10)
        self.buttonEncryptAsc.grid(row=2, column=2, padx=10, pady=10)
        self.label4.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.label2.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.inputMingAsc.grid(row=2, column=1, padx=10, pady=10)
        self.buttonDecryptAsc.grid(row=4, column=2, padx=10, pady=10)
        self.label5.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        self.label3.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.inputMiAsc.grid(row=4, column=1, padx=10, pady=10)

    def encrypt_asc(self):
        key = self.inputKey.get()
        ming = self.inputMingAsc.get()

        if len(key) != 10 or not key.isdigit():
            self.label4.config(text="密钥格式错误，请确保输入十位数字",fg="red")
            return

        mi = self.sdes.encrypt_asc(ming, key)
        self.label4.config(text="密文是：" + mi)

    def decrypt_asc(self):
        key = self.inputKey.get()
        mi = self.inputMiAsc.get()

        if len(key) != 10 or not key.isdigit():
            self.label5.config(text="密钥格式错误，请确保输入十位数字",fg="red")
            return

        ming = self.sdes.decrypt_asc(mi, key)
        self.label5.config(text="明文是：" + ming)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = StringGUI()
    gui.run()
