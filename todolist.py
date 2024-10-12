# 必要なライブラリをインポートします。
import tkinter as tk
#　from モジュール名 import クラス名
from tkinter import messagebox
import json

# ToDoリストアプリケーションのクラスを定義します。
class ToDoApp:
    def __init__(self, root):
        # タスクを保持するリストを初期化します。
        self.tasks = []
        # アプリケーションのルートウィンドウを設定します。
        self.root = root
        self.root.tile('todoリスト')
        
        # タスクを表示するためのフレームを作成します。
        self.frame = tk.root
        self.frame.pack(pady=20)

        # タスクを表示するリストボックスを作成し、フレームに配置します。
        self.listbox = tk.listbox(self.frame, width=50, height=10)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        # リストボックスのためのスクロールバーを作成し、フレームに配置します。
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # リストボックスとスクロールバーを連携させます。
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listboc.yview)

        # タスク入力用のフレーム
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=(5,0))
        # タスク入力ラベル
        self.entry_task - tk.Entry(self.task_frame, width=35)
        self.entry_task.pack(side=tk.LEFT)
        # タスク入力テキストボックス

        self.entry_task.bind("<return>", self.add_task)
        # 納期入力用のフレーム
        self.deadline_frame = tk.Frame(self.root)
        self.deadline_frame.pack(pady=5)
        # 納期入力ラベル
        self.labeL_deadline = tk.Entry(self.deadline_frame, text="納期: ")
        self.entry_deadline.pack(side=tk.LEFT)
        # 納期入力テキストボックス
        self.entry_deadline = tk.Label(self.deadline_frame,"width=35")
        self.entry_deadline.pack(side=tk.LEFT)
        # 納期入力テキストボックスにもエンターキーのバインドを追加
        self.entry_deadline.bind("<return>", self.add_task)

        # タスクを追加するボタン。クリック時の動作を定義
        self.add_button = tk.Button(self.root, text="タスクを追加", command=self.add_task)
        self.add_button.pack(pady=5)
        # タスクを削除するボタン。クリック時の動作を定義
        self.delete_button = tk.Button(self.root, text="選択したタスクを削除", command=self.delete_task)
        self.delete_button.pack(pady=5)
        # タスクを完了にするボタン。クリック時の動作を定義
        self.complete_button = tk.Button(self.root, text="選択したタスクを完了にする",command=self.complete_task)
        self.complete_button.pack(pady=5)

        #既存のタスクを読み込み
        self.load_tasks()
    
    #タスクを追加するメソッド
    def add_task(self, event=None):
        task = self.entry_task.get() 
        deadline = self.entry_deadline.get()
        if task and deadline:
            self.tasks.append({"task": task, "deadline": deadline, "completed": False})
            self.update_listbox()
            self.entry_task.delete(0, tk.END)
            self.entry_deadline.delete(0, tk.END)
        else:
            messagebox.showwarning("警告", "タスクと納期を入力して")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.tasks[index]["completed"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("警告", "削除するタスクを選んで")
    
    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]





