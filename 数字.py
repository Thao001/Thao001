import tkinter as tk
from SDES import SDES


class NumericGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("数字加密解密")
        self.root.geometry("600x400")
        self.sdes = SDES()

        self.initUI()

    def initUI(self):
        font = ("宋体", 14)

        self.inputKey = tk.Entry(self.root, font=font, width=20)
        self.inputMing = tk.Entry(self.root, font=font, width=20)
        self.inputMi = tk.Entry(self.root, font=font, width=20)

        self.buttonEncrypt = tk.Button(self.root, text="加密", font=font, command=self.encrypt, bg="green", fg="white")
        self.buttonDecrypt = tk.Button(self.root, text="解密", font=font, command=self.decrypt, bg="green", fg="white")

        self.label1 = tk.Label(self.root, text="请输入十位的密钥:", font=font)
        self.label2 = tk.Label(self.root, text="请输入八位的明文:", font=font)
        self.label3 = tk.Label(self.root, text="请输入八位的密文:", font=font)
        self.label4 = tk.Label(self.root, text="", font=font)
        self.label5 = tk.Label(self.root, text="", font=font)

        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.inputKey.grid(row=0, column=1, padx=10, pady=10)
        self.buttonEncrypt.grid(row=2, column=2, padx=10, pady=10)
        self.label4.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.label2.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.inputMing.grid(row=2, column=1, padx=10, pady=10)
        self.buttonDecrypt.grid(row=4, column=2, padx=10, pady=10)
        self.label5.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        self.label3.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.inputMi.grid(row=4, column=1, padx=10, pady=10)

    def encrypt(self):
        key = self.inputKey.get()
        ming = self.inputMing.get()

        if len(key) != 10 or not key.isdigit():
            self.label4.config(text="密钥格式错误，请确保输入十位数字",fg="red")
            return
        elif len(ming) != 8 or not ming.isdigit():
            self.label4.config(text="明文格式错误，请确保输入八位数字",fg="red")
            return

        mi = self.sdes.encrypt(ming, key)
        self.label4.config(text="密文是：" + mi)

    def decrypt(self):
        key = self.inputKey.get()
        mi = self.inputMi.get()

        if len(key) != 10 or not key.isdigit():
            self.label5.config(text="密钥格式错误，请确保输入十位数字",fg="red")
            return
        elif len(mi) != 8 or not mi.isdigit():
            self.label5.config(text="密文格式错误，请确保输入八位数字",fg="red")
            return

        ming = self.sdes.decrypt(mi, key)
        self.label5.config(text="明文是：" + ming)

    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    gui = NumericGUI()
    gui.run()