from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class ToDoList(App):
    def __init__(self, **kwargs):
        super(ToDoList, self).__init__(**kwargs)
        self.tasks = []

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        title_label = Label(text="TO-DO App", color=(1, 1, 0, 1), font_size='18sp', size_hint_y=None, height=40)
        self.layout.add_widget(title_label)
        self.task_input = TextInput(hint_text='Enter task here', font_size='16sp', size_hint_y=None, height=40)
        self.layout.add_widget(self.task_input)
        self.add_button = Button(text='Enter', font_size='16sp', size_hint_y=None, height=40)
        self.add_button.bind(on_press=self.add_task)
        self.layout.add_widget(self.add_button)
        self.task_list = ListBox()
        self.layout.add_widget(self.task_list)
        delete_button = Button(text='Delete', font_size='16sp', size_hint_y=None, height=40)
        delete_button.bind(on_press=self.remove_task)
        self.layout.add_widget(delete_button)
        exit_button = Button(text='Exit', font_size='16sp', size_hint_y=None, height=40,)
        exit_button.bind(on_press=self.stop)
        self.layout.add_widget(exit_button)
        return self.layout

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            self.tasks.append(task_text)
            self.task_input.text = ''
            self.update_task_list()

    def update_task_list(self):
        self.task_list.clear_widgets()
        for task in self.tasks:
            task_label = Label(text=task, font_size='16sp', size_hint_y=None, height=40)
            task_label.bind(on_touch_down=self.select_task)
            self.task_list.add_widget(task_label)

    def select_task(self, instance, touch):
        if instance.collide_point(*touch.pos):
            for child in self.task_list.children:
                if child == instance:
                    child.background_color = (0.5, 0.5, 1, 1)
                else:
                    child.background_color = (1, 1, 1, 1)

    def remove_task(self, instance):
        selected_task = None
        for child in self.task_list.children:
            if hasattr(child, 'background_color') and child.background_color == (0.5, 0.5, 1, 1):
                selected_task = child.text
                break

        if selected_task:
            self.tasks.remove(selected_task)
            self.update_task_list()


class ListBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ListBox, self).__init__(**kwargs)
        self.orientation = 'vertical'

    def add_widget(self, widget, index=0, canvas=None):
        widget.size_hint_y = None
        widget.height = 40
        super(ListBox, self).add_widget(widget, index=index, canvas=canvas)


if __name__ == '__main__':
    ToDoList().run()
