from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class MarksCalculator(App):

    def build(self):
        Window.softinput_mode = "below_target"

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        title = Label(
            text="STUDENT MARKS\nCALCULATOR",
            font_size=28,
            bold=True,
            size_hint_y=None,
            height=90
        )
        root.add_widget(title)

        scroll = ScrollView()

        form = GridLayout(
            cols=2,
            spacing=8,
            padding=5,
            size_hint_y=None
        )
        form.bind(minimum_height=form.setter("height"))

        self.entries = {}

        subjects = [
            "Student Name",
            "Roll Number",
            "Maths Marks",
            "Science Marks",
            "English Marks",
            "Hindi Marks",
            "Computer Marks"
        ]

        for subject in subjects:
            form.add_widget(
                Label(
                    text=subject,
                    font_size=17
                )
            )

            entry = TextInput(
                multiline=False,
                font_size=17,
                size_hint_y=None,
                height=50
            )

            self.entries[subject] = entry
            form.add_widget(entry)

        scroll.add_widget(form)
        root.add_widget(scroll)

        buttons = BoxLayout(
            size_hint_y=None,
            height=55,
            spacing=8
        )

        calculate = Button(
            text="CALCULATE",
            font_size=17
        )
        calculate.bind(on_press=self.calculate)

        clear = Button(
            text="CLEAR",
            font_size=17
        )
        clear.bind(on_press=self.clear)

        buttons.add_widget(calculate)
        buttons.add_widget(clear)

        root.add_widget(buttons)

        self.result = Label(
            text="RESULT",
            font_size=18,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=180
        )

        self.result.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        root.add_widget(self.result)

        return root

    def calculate(self, instance):

        try:
            name = self.entries["Student Name"].text.strip()
            roll = self.entries["Roll Number"].text.strip()

            if not name or not roll:
                self.result.text = "Please enter Student Name and Roll Number."
                return

            marks = []

            for subject in [
                "Maths Marks",
                "Science Marks",
                "English Marks",
                "Hindi Marks",
                "Computer Marks"
            ]:
                value = int(self.entries[subject].text)

                if value < 0 or value > 100:
                    self.result.text = "Marks must be between 0 and 100."
                    return

                marks.append(value)

            total = sum(marks)
            percentage = total / 5

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            result = "PASS" if all(m >= 33 for m in marks) else "FAIL"

            self.result.text = (
                f"STUDENT REPORT\n\n"
                f"Student: {name}\n"
                f"Roll No: {roll}\n"
                f"Total Marks: {total} / 500\n"
                f"Percentage: {percentage:.2f}%\n"
                f"Grade: {grade}\n"
                f"Result: {result}"
            )

        except ValueError:
            self.result.text = "Please enter valid marks."

    def clear(self, instance):

        for entry in self.entries.values():
            entry.text = ""

        self.result.text = "RESULT"


if __name__ == "__main__":
    MarksCalculator().run()