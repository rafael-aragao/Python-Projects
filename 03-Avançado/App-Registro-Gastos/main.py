from kivy.config import Config
Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '736')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivymd.uix.list import MDListItem, MDListItemHeadlineText
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer
from kivymd.uix.button import MDButton, MDButtonText
from io import BytesIO
import json
import os
import matplotlib.pyplot as plt

DATA_FILE = 'expenses.json'

def save_data(expenses):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, ensure_ascii=False, indent=4)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    return []

class ExpenseRegisterApp(MDApp):
    total = StringProperty("R$ 0.00")

    def build(self):
        return Builder.load_file("main.kv")
    
    def on_start(self):
        self.load_expenses()
    
    def add_expense(self):
        screen = self.root.get_screen('initial_screen')
        description = screen.ids.description.text
        category = screen.ids.category.text
        value_text = screen.ids.value.text

        if description and category and value_text:
            try:
                value = float(value_text)
                new_expense = {"description": description, "category": category, "value": value}

                expenses = load_data()
                expenses.append(new_expense)
                save_data(expenses)

                screen.ids.description.text = ""
                screen.ids.category.text = ""
                screen.ids.value.text = ""

                self.load_expenses()
            except ValueError:
                self.show_error_dialog("Valor Invalido. Favor entrar com um número válido.")
        else:
            self.show_error_dialog("Por Favor Preencha todos os Campos     ")
    
    def load_expenses(self):
        history_screen = self.root.get_screen('history_screen')
        history_screen.ids.expense_list.clear_widgets()

        expenses = load_data()
        total = 0

        for expense in expenses:
            item = MDListItem()
            item.add_widget(MDListItemHeadlineText(
                text=f"{expense['description']} - R${expense['value']:.2f} ({expense['category']})"))
            history_screen.ids.expense_list.add_widget(item)
            total += expense['value']
        self.total = f"R$ {total:.2f}"
    
    def open_chart(self):
        expenses = load_data()
        categories = {}

        for expense in expenses:
            cat = expense['category']
            categories[cat] = categories.get(cat, 0) + expense['value']
        
        if not categories:
            self.show_error_dialog("No expenses recorded to generate the chart.")
            return
        
        labels = list(categories.keys())
        sizes = list(categories.values())

        plt.figure(figsize=(5, 5))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')

        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        plt.close()

        core_image = CoreImage(buffer, ext='png')
        image_widget = Image(
            texture=core_image.texture, 
            size_hint=(None, None),
            size=(400, 400),
            pos_hint={'center_x': 0.0, 'center_y': 1.0})
        
        content = MDBoxLayout(orientation='vertical')
        content.add_widget(image_widget)

        dialog = MDDialog(
            content,
            MDDialogButtonContainer(
                on_release=lambda x: dialog.dismiss()
            ),
            size_hint=(0.95, 0.45),
        )
        dialog.open()

    def show_error_dialog(self, message):

        dialog = MDDialog(
            MDDialogHeadlineText(
                text="Attention!",
                halign="center",
                theme_text_color="Custom",
                text_color="red",
                theme_font_name="Custom",
                font_name="BebasNeue-Regular.ttf",
            ),
            MDDialogHeadlineText(
                text=message,
                halign="center",
                theme_text_color="Custom",
                text_color="black",
                theme_font_name="Custom",
                font_name="BebasNeue-Regular.ttf",
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Close"),
                    style="text",
                    on_release=lambda x: dialog.dismiss()
                ),
                spacing="2dp",
            ),
            size_hint=(0.6, 0.5),
        )
        dialog.open()

if __name__ == "__main__":
    ExpenseRegisterApp().run()