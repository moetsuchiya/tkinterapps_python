tasks = []

task = input('タスクを入力してね')
deadline = input('期日を入力してね')

while task != '': #タスクがなければループを抜けます
    if task and deadline: # タスクと納期の両方が入力されていたら
        tasks.append({'task': task, 'deadline': deadline, 'completed': False})

    print() #ただの改行
    print('タスクに追加があれば、記入してね')

    task = input('タスクを入力してね')
    deadline = input('期日を入力してね')

print()
print('タスク情報')
print(tasks)

tasks[0]['completed'] = True

for task in tasks:
    task_info = f'{task['task']} [期限: {task['deadline']}]'
    if task['completed']:
        task_info += ' [完了]'
    print(task_info)

