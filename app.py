import tkinter as tk
from tkinter import messagebox, filedialog


def get_result():
    try:
        name = name_entry.get().strip()
        roll = roll_entry.get().strip()

        if not name or not roll:
            messagebox.showwarning(
                "Warning",
                "Student Name aur Roll Number bharo!"
            )
            return None

        marks = [
            int(math_entry.get()),
            int(science_entry.get()),
            int(english_entry.get()),
            int(hindi_entry.get()),
            int(computer_entry.get())
        ]

        if any(m < 0 or m > 100 for m in marks):
            messagebox.showerror(
                "Error",
                "Marks 0 se 100 ke beech hone chahiye."
            )
            return None

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

        return name, roll, marks, total, percentage, grade, result

    except ValueError:
        messagebox.showerror(
            "Error",
            "Marks me sirf numbers likho."
        )
        return None


def calculate():
    data = get_result()

    if data is None:
        return

    name, roll, marks, total, percentage, grade, result = data

    report_text.config(
        text=(
            "STUDENT REPORT\n\n"
            f"Student: {name}\n"
            f"Roll No: {roll}\n\n"
            f"Total Marks: {total} / 500\n"
            f"Percentage: {percentage:.2f}%\n"
            f"Grade: {grade}\n"
            f"Result: {result}"
        ),
        fg="green" if result == "PASS" else "red"
    )


def save_report():
    data = get_result()

    if data is None:
        return

    name, roll, marks, total, percentage, grade, result = data

    report = (
        "============================\n"
        "       STUDENT REPORT\n"
        "============================\n\n"
        f"Student Name : {name}\n"
        f"Roll Number  : {roll}\n\n"
        f"Maths        : {marks[0]}\n"
        f"Science      : {marks[1]}\n"
        f"English      : {marks[2]}\n"
        f"Hindi        : {marks[3]}\n"
        f"Computer     : {marks[4]}\n\n"
        f"Total Marks  : {total} / 500\n"
        f"Percentage   : {percentage:.2f}%\n"
        f"Grade        : {grade}\n"
        f"Result       : {result}\n\n"
        "============================\n"
    )

    filename = filedialog.asksaveasfilename(
        title="Save Student Report",
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt")],
        initialfile=name + "_report.txt"
    )

    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)

        messagebox.showinfo(
            "Saved",
            "Student report save ho gayi!"
        )


def clear_all():
    for entry in [
        name_entry,
        roll_entry,
        math_entry,
        science_entry,
        english_entry,
        hindi_entry,
        computer_entry
    ]:
        entry.delete(0, tk.END)

    report_text.config(
        text="RESULT",
        fg="black"
    )


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("Student Marks Calculator")

# Phone-friendly size
root.geometry("360x700")
root.resizable(False, False)
root.configure(bg="lightgray")


# =========================
# TITLE
# =========================

tk.Label(
    root,
    text="STUDENT MARKS\nCALCULATOR",
    font=("Arial", 15, "bold"),
    bg="lightgray",
    justify="center"
).pack(pady=8)


# =========================
# INPUT AREA
# =========================

input_frame = tk.Frame(
    root,
    bg="lightgray"
)

input_frame.pack(
    fill="x",
    padx=8
)


def make_row(label_text):

    row = tk.Frame(
        input_frame,
        bg="lightgray"
    )

    row.pack(
        fill="x",
        pady=2
    )

    tk.Label(
        row,
        text=label_text,
        font=("Arial", 10),
        bg="lightgray",
        width=15,
        anchor="e"
    ).pack(
        side="left",
        padx=2
    )

    entry = tk.Entry(
        row,
        font=("Arial", 11),
        width=15,
        justify="center"
    )

    entry.pack(
        side="left",
        padx=3
    )

    return entry


name_entry = make_row("Student Name")
roll_entry = make_row("Roll Number")
math_entry = make_row("Maths Marks")
science_entry = make_row("Science Marks")
english_entry = make_row("English Marks")
hindi_entry = make_row("Hindi Marks")
computer_entry = make_row("Computer Marks")


# =========================
# BUTTONS
# =========================

tk.Button(
    root,
    text="CALCULATE RESULT",
    command=calculate,
    font=("Arial", 12, "bold"),
    width=25,
    height=1
).pack(pady=5)


tk.Button(
    root,
    text="SAVE REPORT",
    command=save_report,
    font=("Arial", 12, "bold"),
    width=25,
    height=1
).pack(pady=3)


tk.Button(
    root,
    text="CLEAR",
    command=clear_all,
    font=("Arial", 12),
    width=25,
    height=1
).pack(pady=3)


# =========================
# RESULT TITLE
# =========================

tk.Label(
    root,
    text="RESULT",
    font=("Arial", 16, "bold"),
    bg="lightgray"
).pack(pady=5)


# =========================
# RESULT BOX
# =========================

report_text = tk.Label(
    root,
    text="RESULT",
    font=("Arial", 10, "bold"),
    bg="lightgray",
    justify="center",
    relief="solid",
    bd=1,
    width=35,
    height=7,
    padx=5,
    pady=5

)

report_text.pack(
    padx=8,
    pady=3
)


root.mainloop()