from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
import requests

# Configs
import my_config

# KV
kv = '''
#:include ./screens/SignIn/signin.kv
'''

Builder.load_string(kv)


class SignInScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self):
        self.ids.btn_sign_in.icon = "clock-outline"
        self.ids.btn_sign_in.disabled = True
        self.ids.btn_sign_in.text = "Please Wait"

        username = self.ids.username
        password = self.ids.password
        alert = self.ids.alert
        alert_text = self.ids.alert_text

        if username.text == "" or password.text == "":
            alert_text.text = "Username and Password could not be empty"
            animation_text = Animation(opacity=1, duration=0.5)
            animation_alert = Animation(height=60, duration=0.5)
            animation_alert.start(alert)
            animation_text.start(alert_text)

            self.ids.btn_sign_in.icon = "account-arrow-right"
            self.ids.btn_sign_in.text = "SIGN IN"
            self.ids.btn_sign_in.disabled = False

        else:
            try:
                animation_text = Animation(opacity=0, duration=0.5)
                animation_alert = Animation(height=30, duration=0.5)
                animation_alert.start(alert)
                animation_text.start(alert_text)

                response = requests.post(my_config.API_URL, data={'username': username.text, 'password': password.text})

                if response.status_code == 200:
                    result = response.json()
                    if result['is_valid']:
                        self.manager.current = "dashboard"
                        self.manager.transition.direction = "left"
                    else:
                        alert_text.text = "Username or Password is invalid. Try again with correct credentials"
                        animation_text = Animation(opacity=1, duration=0.5)
                        animation_alert = Animation(height=60, duration=0.5)
                        animation_alert.start(alert)
                        animation_text.start(alert_text)
                else:
                    raise Exception("Something was wrong. Try again in few seconds" + " " + str(response.status_code))

                self.ids.btn_sign_in.icon = "account-arrow-right"
                self.ids.btn_sign_in.text = "SIGN IN"
                self.ids.btn_sign_in.disabled = False

            except Exception as e:
                alert_text.text = "Something was wrong. Try again in few seconds"
                print(e)
                animation_text = Animation(opacity=1, duration=0.5)
                animation_alert = Animation(height=60, duration=0.5)
                animation_alert.start(alert)
                animation_text.start(alert_text)

                self.ids.btn_sign_in.icon = "account-arrow-right"
                self.ids.btn_sign_in.text = "SIGN IN"
                self.ids.btn_sign_in.disabled = False
