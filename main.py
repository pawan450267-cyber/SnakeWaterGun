import random
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

class Game(BoxLayout):

    user_choice = StringProperty("None")
    computer_choice = StringProperty("None")
    result = StringProperty("Choose Snake, Water or Gun")

    user_score = NumericProperty(0)
    computer_score = NumericProperty(0)

    def play(self, choice):

        choices = {
            "Snake": 1,
            "Water": 2,
            "Gun": 0
        }

        reverse = {
            1: "Snake",
            2: "Water",
            0: "Gun"
        }

        computer = random.choice([0,1,2])

        self.user_choice = choice
        self.computer_choice = reverse[computer]

        you = choices[choice]

        if computer == you:
            self.result = "Game Draw"

        elif (computer == 1 and you == 0) or \
             (computer == 2 and you == 1) or \
             (computer == 0 and you == 2):

            self.result = "🎉 You Won"
            self.user_score += 1

        else:
            self.result = "😢 You Lose"
            self.computer_score += 1


class SnakeWaterGun(App):
    def build(self):
        return Game()

SnakeWaterGun().run()
