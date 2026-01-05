# Day 13: OOP + Backend Base (User System)

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password   
        self.role = role

    def check_password(self, input_password):
        return self.password == input_password

    def is_admin(self):
        return self.role == "admin"


class UserManager:
    def __init__(self):
        self.users = {}   # username : User object

    def register(self, username, password, role="user"):
        if username in self.users:
            return " User already exists"
        self.users[username] = User(username, password, role)
        return " User registered successfully"

    def login(self, username, password):
        user = self.users.get(username)
        if not user:
            return "User not found"
        if user.check_password(password):
            return f"Login successful ({user.role})"
        return " Wrong password"


# Testing
manager = UserManager()

print(manager.register("krushna", "1234"))
print(manager.register("admin", "admin123", role="admin"))

print(manager.login("krushna", "1234"))
print(manager.login("admin", "wrongpass"))
print(manager.login("admin", "admin123"))
