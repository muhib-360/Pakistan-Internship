import sqlite3.dbapi2
import customtkinter as ctk
import time
from datetime import datetime
import sqlite3

app = ctk.CTk()
app.title("Quiz App")
app._set_appearance_mode('dark')
app.geometry("800x550")
ctk.set_appearance_mode('dark')
app.resizable(width=False , height=False)
ctk.set_default_color_theme("green")



db = "E:\\Internships\\Pakistan Internship\\QuizApp\\quizapp.db"
conn = sqlite3.connect(db)
c = conn.cursor()

class Main:
    def __init__(self):
        self.main_frame = ctk.CTkFrame(master=app, corner_radius=10 , bg_color="transparent" , width=600)
        self.main_label = ctk.CTkLabel(master=self.main_frame,text=" |  Quiz Application  | ", font=("Arial" , 20) ,  corner_radius=80 , anchor="center" , bg_color="transparent") 
        self.main_button_frame = ctk.CTkFrame(master=app , corner_radius=10 , bg_color="transparent" , width=10 , height=10)
        self.main_button = ctk.CTkButton(master=self.main_button_frame ,text="Next", corner_radius= 10 ,command=lambda:self.hide_main_page(),anchor="center")
        self.exit_button = ctk.CTkButton(master=self.main_button_frame , corner_radius=10 , text="Exit" ,  command=self.exit_app , anchor="center" , fg_color="#FFFFFF" , hover=True , hover_color="#f4f4f4", text_color="#000000" )
        self.terms_label = ctk.CTkLabel(master=self.main_frame, corner_radius=10 ,anchor="center", text="Terms & Conditions" , font=("Bowlby" , 15))
        self.main_frame.pack(pady =10)
        self.main_label.pack(pady =10)
        self.terms_label.pack(pady = 10)
        self.text_box = ctk.CTkTextbox(master=self.main_frame , wrap="word", corner_radius= 10, activate_scrollbars=True , height=350 , width=450)
        # self.main_button.pack(pady =10)
        self.text_box.pack(pady =10 , fill = "x" , expand = True , side = "bottom")
        message1 = """Thank you for choosing the Quiz Application! We are committed to protecting your privacy and ensuring your experience is safe and enjoyable. This privacy policy explains how we collect, use, and safeguard your information when you use our app.

1. Information We Collect

The Quiz Application does not collect any personal information from users. The app only processes the game data, which includes:

Your answers
Quiz progress (i.e., number of attempts)
Past score and metrics
    
2. Use of Data

All data processed within the app is used solely for the user's intent and is not transmitted to any external servers or third parties.

3. Data Security

We value your trust in providing us with your data, and we strive to use commercially acceptable means toprotect it. However, remember that no method of transmission over the internet or method of electronic storageis 100% secure and reliable, and we cannot guarantee its absolute security.

4. Third-Party Services

The Quiz Application does not use third-party services that collect or track user data."""


        self.text_box.insert(ctk.END,message1)
        self.text_box.configure(state = "disabled" )

    def show_main_screen(self):
        self.main_frame.pack(fill = 'y')
        self.main_label.pack()
        self.terms_label.pack()
        self.main_button_frame.pack(pady = 10 , padx = 10 , fill = "x")
        self.exit_button.pack(side = "left" , padx = 60)
        self.main_button.pack(padx = 60 , side = "right")


    def exit_app(self):
        app.quit()

    def hide_main_page(self):
        self.main_frame.pack_forget()
        self.main_button_frame.pack_forget()
        second.second_frame.pack()
        second.start_button_frame.pack()


class SecondScreen:
    def __init__(self):
        self.second_frame = ctk.CTkFrame(master=app ,corner_radius= 10 , bg_color="transparent" )
        self.quiz_label = ctk.CTkLabel(master=self.second_frame ,text="Quiz Form" ,font=("Bowlby" , 30) , corner_radius=10 , anchor="center")
        self.quiz_info  =ctk.CTkLabel(master=self.second_frame , text="Note : Fill the details carefully, ensuring the input contains no extra spaces or special symbols. This can lead to errors in the backend logics.")
        self.start_button_frame = ctk.CTkFrame(master=app , corner_radius=10)
        self.start_button = ctk.CTkButton(master=self.start_button_frame , text="Submit" , corner_radius=10 , command = self.handle_submit_button)
        self.back_button = ctk.CTkButton(master=self.start_button_frame , text="Back" , corner_radius=10,command=lambda:self.show_back_screen())
        self.past_score_btn = ctk.CTkButton(master=self.second_frame , corner_radius=10 , text="Past Scores" , font=("Bowlby" , 18) , border_spacing=1 , command=lambda:self.handle_past_button()) 

        self.quiz_frame = ctk.CTkFrame(master=app , corner_radius=10 , height=200)
        self.quiz_frame2 = ctk.CTkFrame(master=self.quiz_frame , corner_radius=10)
        self.combo_box = ctk.CTkComboBox(master=self.quiz_frame2 ,values=["Science" , "History" , "General Knowledge"])
        self.combo_box.set("Select the category")
        self.name_label = ctk.CTkLabel(master=self.quiz_frame2  , corner_radius=10 , text="User Name : ")
        self.id_label = ctk.CTkLabel(master=self.quiz_frame2  , corner_radius=10 ,anchor='ne', text="User ID : ")
        self.quiz_details = ctk.CTkLabel(master=self.second_frame , text="Quiz Details ")

        self.id_box = ctk.CTkEntry(master=self.quiz_frame2 ,corner_radius=10 , border_color="red" , placeholder_text="Enter your ID")
        self.name_box = ctk.CTkEntry(master=self.quiz_frame2 , corner_radius=10,border_color="blue" , placeholder_text="Enter your name  ")     
        self.select_label = ctk.CTkLabel(master=self.quiz_frame2 , text="Select the category")
        self.quiz_id = 0



    def handle_past_button(self):
        new_window = ctk.CTkToplevel(self.quiz_frame)
        new_window.geometry("500x500")
        new_window._set_appearance_mode('dark')
        self.get_past_scores()      
        self.score_frame = ctk.CTkFrame(master=new_window , corner_radius=10 , bg_color='transparent')

        self.score_label = ctk.CTkLabel(master=new_window ,corner_radius=10 , anchor='center' , text="Past Score : ")
        self.show_past_score = ctk.CTkLabel(master=new_window , text=self.past_score , bg_color='transparent' , font=("Bowlby" ,18))
        self.score_frame.pack(pady = 10 , side ='top')
        self.score_label.pack(pady = 10)
        self.show_past_score.pack(pady =10)

    def get_past_scores(self):
        c = conn.cursor()
        # Query to fetch the score from the database
        try:
            # Fetch the score for the specific user
            result = c.execute("SELECT score FROM scores WHERE user_id == (?)", (second.user_id,)).fetchone()
            
            # Store the score if available
            if result:
                self.past_score = result[0]  # Get the score 
            else:
                self.past_score = None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.past_score = None
        finally:
            c.close()




    def handle_submit_button(self):
        self.hide_all()
        self.store_user_details()
        self.hide_all()
        # play = PlayQuiz()


    def store_user_details(self):
        self.user_id = self.id_box.get()
        self.user_name = self.name_box.get()
        self.selected_category = self.combo_box.get()

        c.execute("INSERT INTO users (user_id, user_name) VALUES (?, ?)", (self.user_id, self.user_name))
        c.execute("INSERT INTO scores (category , user_id , quiz_id) VALUES (? , ? , ?)", (self.selected_category , self.user_id , self.quiz_id+1))
        conn.commit()
        c.close()

    def check_repeated_users(self):
        c.execute("Select * from ")

    def show_start_page(self):
        self.second_frame.pack(pady = 10 , fill = "y")
        self.quiz_label.pack(pady = 10)
        info_message = """
You guess the number and write into textbox. The computer will check if it matches the output. 

If you guessed correctly, you'll win. Otherwise , You Lose."""

        self.quiz_info.pack(fill = 'y')
        self.quiz_frame.pack(padx = 10,pady = 10 , fill = 'both')
        self.quiz_frame2.pack(fill = 'x')
        self.id_label.pack()
        self.id_box.pack()
        self.name_label.pack()
        self.name_box.pack()
        self.select_label.pack()
        self.combo_box.pack()
        self.combo_box.configure()
        self.start_button_frame.pack(fill = "x"  , pady = 25)
        self.back_button.pack(side = "left" , padx = 60)
        self.start_button.pack(side = "right", padx = 70)
        self.past_score_btn.pack(side = "right" , padx = 20)


    def show_back_screen(self):
        self.second_frame.pack_forget()
        self.start_button_frame.pack_forget()
        main.show_main_screen()

    def hide_start_screen(self):
        self.start_button_frame.pack_forget()
        self.start_button.pack_forget()
        self.back_button.pack_forget()
        self.second_frame.pack_forget()
        self.quiz_info.pack_forget()
        self.quiz_frame.pack_forget()
        self.quiz_frame2.pack_forget()
        self.id_label.pack_forget()
        self.id_box.pack_forget()
        self.name_label.pack_forget()
        self.name_box.pack_forget()
        self.select_label.pack_forget()
        self.combo_box.pack_forget()

    def hide_all(self):
        self.second_frame.pack_forget()
        self.start_button_frame.pack_forget()
        main.main_frame.pack_forget()
        main.main_button_frame.pack_forget()


class Quiz:
    def __init__(self):
        self.quiz_window_frame = ctk.CTkFrame(master=app , corner_radius=10 , bg_color="transparent" ,border_width=2)
        self.quiz_info = ctk.CTkLabel(master=self.quiz_window_frame , corner_radius=10 ,text="Quiz Info" , font=("Bowlby" , 25))
        self.sub_head = ctk.CTkLabel(master=self.quiz_window_frame , corner_radius=10 , text="Points to Consider" , font=("Bowlby" , 15))
        self.quiz_notes1 = ctk.CTkLabel(master=self.quiz_window_frame , text=" The quiz contains 10 mcqs, each having 2 mark weightage. There will be a quiz timer for 2 minutes. ")
        self.quiz_notes2 = ctk.CTkLabel(master=self.quiz_window_frame ,corner_radius=10 , text="Please make sure to complete your quiz on time. Quiz will automatically submit to the backend servers and you'll not be able to access it later.")
        self.quiz_notes3 = ctk.CTkLabel(master=self.quiz_window_frame, corner_radius=10 , text="Note : Select only the one correct option. After starting the quiz, you cannot go back !. Make sure you select each option correctly.")
        self.start_button = ctk.CTkButton(master=self.quiz_window_frame , corner_radius=10 , anchor="center" , text="Start Quiz" , hover=True, hover_color="white" , command=lambda:self.handle_button_click)


    def handle_button_click(self):
        self.hide_previous_all()
        self.store_info()
        play.show_the_quiz()


    def store_info(self):
        c.execute()

    def show_quiz_window(self):
        self.quiz_window_frame.pack(pady = 10 , fill = 'both')
        self.quiz_info.pack(pady = 10)
        self.sub_head.pack(pady =10)
        self.quiz_notes1.pack(fill = 'both' , pady = 10)
        self.quiz_notes2.pack(fill = "both" , pady = 10)
        self.quiz_notes3.pack(fill = "both" , pady = 10)
        self.start_button.pack(side = "bottom" , pady = 10)
        # self.past_score_btn.pack(side = 'bottom' , pady = 10)

    def hide_previous_all(self):
        main.hide_main_page()
        second.hide_all()
        second.hide_start_screen()
        quiz.quiz_window_frame.pack_forget()
        quiz.quiz_info.pack_forget()
        quiz.quiz_notes1.pack_forget()
        quiz.quiz_notes2.pack_forget()



class PlayQuiz:
    def __init__(self):
        self.root = app
        self.head_frame = ctk.CTkFrame(master=app , corner_radius=10 , bg_color="transparent")
        self.heading = ctk.CTkLabel(master=self.head_frame, corner_radius=10 , text="Choose the correct option" , font=("Bowlby" , 25) , anchor='n')
        self.head_frame.pack(pady=10 , fill = 'x')
        self.heading.pack(side = 'top' , pady = 15)

        self.start_time = time.time()
        self.radio_button = ctk.CTkRadioButton(master=app, corner_radius=10)
        self.canvas = ctk.CTkCanvas(app ,  bg = "#90EE90")
        self.canvas.pack(side='top' , fill='both', expand=True)
        self.scrollbar = ctk.CTkScrollbar(master=self.canvas , orientation='vertical' , command=self.canvas.yview)
        self.frame = ctk.CTkFrame(self.canvas)
        scrollbar = ctk.CTkScrollbar(master=self.canvas, orientation=ctk.VERTICAL, command=self.canvas.yview, border_spacing=1)
        scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0,0),height=1800 ,width=800, window=self.frame , anchor='nw')
        self.questions = self.fetch_questions()
        self.display_questions(self.questions)
        self.submit_button = ctk.CTkButton(master=self.frame , corner_radius=10 ,font=("Bowlby" , 18), text="Submit",anchor='center' , command=self.handle_button_activity)
        self.submit_button.pack(pady = 60)
        conn.close()
    
    def fetch_questions(self):
        c.execute("Select * from questions")
        return c.fetchall()
    
    def display_questions(self , questions):
        self.selected_options = {}
        for index , question_data in enumerate(questions):
            question_id , category_id , question_text ,option_a , option_b , option_c , option_d , correct_answer = question_data

            self.selected_options[question_id] = ctk.IntVar(value=0)

            question_label = ctk.CTkLabel(master=self.frame , text=f"Q.{index+1}:{question_text}" , font=("Bowlby" , 15))
            question_label.pack(pady = 20)

            selected_option = ctk.StringVar()
            ctk.CTkRadioButton(master=self.frame, text=option_a, variable=self.selected_options[question_id], value=option_a).pack(anchor='w', padx=20)
            ctk.CTkRadioButton(master=self.frame, text=option_b, variable=selected_option, value=option_b).pack(anchor='w', padx=20)
            ctk.CTkRadioButton(master=self.frame, text = option_c, variable=selected_option, value=option_c).pack(anchor='w', padx=20)
            ctk.CTkRadioButton(master=self.frame, text=option_d, variable=selected_option, value=option_d).pack(anchor='w', padx=20)

    def handle_button_activity(self):
        self.store_score()
        self.submit_quiz()

    def submit_quiz(self):
        self.store_score()
        self.submit_quiz()


    def show_the_quiz(self):
        print("Running ... ")

    def store_score(username, score):
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute('INSERT INTO scores (username, score, date) VALUES (?, ?, ?)', (username, score, current_date))
        conn.commit()
        c.close()

    def hide_all_previous(self):
        main.hide_main_page()
        second.hide_all()
        second.hide_start_screen()
        quiz.hide_previous_all()

countdown_time = 120  # This will track the remaining seconds
class TimerApp:
    def __init__(self):
        self.root = app
        self.timer_label = ctk.CTkLabel(play.head_frame, text="02:00", font=("Helvetica", 18) ,bg_color="#C5E8B7", text_color="#E65539", anchor='center')
        self.timer_label.pack(padx = 10,side = 'right')
        self.update_timer()

# Function to update the countdown
    def update_timer(self):
        global countdown_time  # Access the global variable

    # Convert seconds to minutes and seconds
        minutes, seconds = divmod(countdown_time, 60)
        self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")

        if countdown_time > 0:
            countdown_time -= 1  # Decrement the countdown time
            self.root.after(1000, self.update_timer)  # Call this function again after 1 second
        else:
            self.timer_label.configure(text="Time's Up!")  # When timer reaches 0
            print("Quiz Finished!")  # You can add more actions here

main = Main()
if main.show_main_screen():
    main.hide_main_page()
second = SecondScreen()
if second.show_start_page():
    second.hide_start_screen()
quiz = Quiz()
if quiz.show_quiz_window():
    quiz.hide_previous_all()

play = PlayQuiz()
timer = TimerApp()


app.mainloop()


