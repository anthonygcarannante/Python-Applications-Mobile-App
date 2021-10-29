from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    # Points to "Sign Up" screen in design.kv file
    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "sign_up_screen"
    
    def login(self, uname, pword):
        with open('users.json', 'r') as file:
            users = json.load(file)
        
        # Check if username is in list of users in json library
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong username or password!"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)

        # Add new user dictionary to users
        users[uname] = {'username': uname, 
                        'password': pword,
                        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        # Rewrite json file to add new user
        with open("users.json", "w") as file:
            json.dump(users, file)

        self.manager.transition.direction = 'left'
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):

        # Switch back to login screen
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()