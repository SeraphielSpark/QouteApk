# main.py
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from plyer import tts
from datetime import datetime
import os

# Set screen size for desktop testing (not needed on mobile)
Window.size = (400, 300)

categories_files = {
    "Spirituality": "spirituality.txt",
    "Wisdom": "wisdom.txt",
    "Motivation": "motivation.txt",
    "Creativity": "creativity.txt",
    "Focus": "focus.txt",
    "Happiness": "happiness.txt"
}

def load_quotes():
    quotes = {}
    for category, filename in categories_files.items():
        try:
            with open(filename, encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
                quotes[category] = lines
        except FileNotFoundError:
            print(f"Missing file: {filename}")
            quotes[category] = []
    return quotes

class QuoteMystic(BoxLayout):
    def __init__(self, quotes, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.quotes = quotes
        self.categories = list(quotes.keys())
        self.label = Label(
            text="QuoteMystic\nTap to start today's session",
            halign='center',
            valign='middle',
            font_size=18
        )
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

        self.bind(on_touch_down=self.on_touch)

    def speak(self, text):
        tts.speak(text)

    def show_daily_quotes(self, *args):
        day = datetime.now().day
        display = ""
        for category in self.categories:
            quotes_list = self.quotes.get(category, [])
            if quotes_list:
                index = (day - 1) % len(quotes_list)
                quote = quotes_list[index]
                display += f"\n[b]{category}[/b]: {quote}\n"
                self.speak(quote)
        self.label.text = f"[b]QuoteMystic Today - {datetime.now().strftime('%Y-%m-%d')}[/b]\n{display}"
        self.label.markup = True

    def on_touch(self, *args):
        self.show_daily_quotes()

class QuoteMysticApp(App):
    def build(self):
        quotes = load_quotes()
        return QuoteMystic(quotes)

if __name__ == '__main__':
    QuoteMysticApp().run()
