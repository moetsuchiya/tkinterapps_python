import tkinter as tk

def button_click(symbol):
    current = display_var.get() #get()メソッド: display_varに現在保存されている値を取得する (画面に表示されている現在のテキストを取得)
    if current == "Error": #もし前の計算がエラーだったら
        display_var.set("") #電卓の画面表示を空にする（クリアする） set()メソッド: display_varの値を変更する
        current="" #内部の計算状態(エラー)もリセット
    if symbol == "=":
        try:
            result = eval(current) #eval関数: 入力された文字列を数式として計算する
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif symbol == "C": #入力をクリア
        display_var.set("")
    else:
        display_var.set(current + symbol)

root = tk.Tk()
root.title("電卓")

display_var = tk.StringVar()
#電卓のディスプレイ部分
display = tk.Entry(root, textvariable=display_var, font=("Arial", 18), bd=10, insertwidth=14, justify="right")
display.grid(row=0, colum=0, columspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('7', 2, 3),
    ('1', 3, 0,), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0,), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), padz=20, pady=20,
                       command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, colum=col)

root.mainloop()