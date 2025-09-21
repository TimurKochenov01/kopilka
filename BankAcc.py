class Goal:
    def __init__(self, name, target, category):
        self.name = name
        self.target = target
        self.balance = 0
        self.category = category
        self.status = "активна"

    def add_money(self, n):
        self.balance += n
        if self.balance > self.target:
            self.balance = self.target
    def remove_money(self, n):
        if self.balance >= n:
            self.balance -= n
    def target_percent(self):
        n = self.balance * 100 // self.target
        return n
    def change_target(self):
        if self.balance >= self.target:
            self.status = "выполнено"

    def __str__(self):
        return f"{self.name} ({self.category}): {self.balance}/{self.target} - {self.status}"

class GoalManager:
    def __init__(self):
        self.goals = []
        self.categories = ["Работа", "Здоровье", "Образование", "Путешествия", "Другое"]

    def add_goal(self, name, target, category):
        if category not in self.categories:
            return False

        goal = Goal(name, target, category)
        self.goals.append(goal)
        return True

    def show_goals(self):
        for i, goal in enumerate(self.goals, 1):
            progress = goal.target_percent()
            print(f"{i}. {goal} [{progress}%]")

    def delete_goal(self, index):
        if 0 <= index < len(self.goals):
            del self.goals[index]
            return True
        return False

manager = GoalManager()
manager.add_goal("Новый ноутбук", 100000, "Работа")
manager.add_goal("Отпуск", 50000, "Путешествия")

manager.goals[0].add_money(25000)
manager.goals[0].add_money(75000)
manager.goals[1].add_money(10000)

manager.show_goals()



