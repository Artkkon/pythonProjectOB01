class Task:
    task_list = []

    def __init__(self, name, description, due_date, status='не выполнено'):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status

    def add_to_list(self):
        Task.task_list.append(self)

    def change_status(self):
        if self.status == 'не выполнено':
            self.status = 'выполнено'
        else:
            self.status = 'не выполнено'

    @staticmethod
    def display_current():
        print("Текущие задачи (не выполнено):")
        for task in Task.task_list:
            if task.status == 'не выполнено':
                print(f"Задача: {task.name}")
                print(f"Описание: {task.description}")
                print(f"Дата выполнения: {task.due_date}")
                print(f"Статус: {task.status}")
                print()

# Создание задач и добавление их в общий список
task1 = Task('задача1', 'накормить кошку', '01.01.2025')
task1.add_to_list()
task2 = Task('задача2', 'накормить собаку', '01.01.2025')
task2.add_to_list()
task3 = Task('задача3', 'пробежать полумарафон', '01.01.2025')
task3.add_to_list()

# Отображение текущих задач
Task.display_current()

# Изменение статуса первой задачи
task1.change_status()

# Отображение текущих задач после изменения статуса
Task.display_current()
