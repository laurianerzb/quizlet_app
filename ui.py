from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
FONT_TWO = ("Arial", 10, "bold")
GREEN = 'green'
RED = 'red'


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlet App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR,)
        # create a score label
        self.score_label = Label(text="0", font=FONT_TWO, fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # create a canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Quizlet", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # create a button
        true_img = PhotoImage(file='./images/true.png')
        self.btn_true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.btn_true.grid(row=2, column=0)
        false_img = PhotoImage(file='./images/false.png')
        self.btn_false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.btn_false.grid(row=2, column=1)
        self.btn_exit = Button(text="Exit", highlightthickness=0, command=self.exit_pressed, bg=RED)
        self.btn_exit.grid(row=0, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_pressed(self):
        is_correct = self.quiz.check_answer('True')
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer('False')
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, func=self.get_next_question)

    def exit_pressed(self):
        self.window.destroy()
