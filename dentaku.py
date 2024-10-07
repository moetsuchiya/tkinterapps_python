# as tkでtkinterにエイリアス(短い別名)をつける
import tkinter as tk
#インスタンス = モジュール.クラス() TK:tkinterウィンドウを作成
root = tk.Tk()
#titleはtkクラスのメソッド:ウィンドウのタイトルを設定する
root.title('My Window')


'''
tkinterのコールバック関数は、特定のイベント（ボタンがクリックされたとき）に対して、呼び出される関数のことです。
つまり、ユーザーの操作やイベントが発生した際に実行される
この場合、ボタンがクリックされたらButton clicked!と表示される。
'''
def callback_function():
    print("Button clicked!")
button = tk.Button(root, text="Click me!", command=callback_function)

'''
root変数が使われる理由は、rootがウィジェットの親ウィンドウを指定しているから
tkinterでは、各ウィジェット（ボタン、ラベル、エントリなど）は、
どこに表示されるか（どのウィンドウに属するか）を指定する必要があります。
rootは、通常アプリケーションのメインウィンドウ（Tkクラスのインスタンス）を表しており、
このウィンドウ内に配置するために使われます。
'''
#https://qiita.com/hiratake_0108/items/210d78e8a9f912bfd2cb
#インスタンス = モジュール.クラス()
button = tk.Button(root, text='Click me!', command=callback_function)
label = tk.Label(root, text='Hello, Tkinter!')
entry = tk.Entry(root)

button.pack()
label.grid(row=0, colum=0)
entry.place(x=50, y=50)

'''
StringVar, DoubleVarなどのTkinter変数は、ウィジェットの値を追跡・管理するためのオブジェクトです。
テキストボックスやチェックボックス等のウィジェットと値を関連付けて、値の変更をリアルタイムで追跡できる。
'''
var = tk.StringVar()
label = tk.Label(root, textvariable=var)
var.set("Hello, Tkinter!")

'''
ウィジェットの外観や動作をカスタマイズするために、
各ウィジェットにはさまざまな属性があります。
パラメタの詳細は公式リファレンスを確認ください。
'''
button = tk.Button(root, text="Click me!", bg="blue", fg="white", font=("Arial", 12))
label = tk.Label(root, text="Hello, Tkinter!", padx=10, pady=10, relief="raised")

'''
Tkinterアプリケーションのメインループを実行します。
メインループを実行しないとコードの処理が終了しきった段階でGUI画面が閉じられてしまいます。
'''
root.mainloop()