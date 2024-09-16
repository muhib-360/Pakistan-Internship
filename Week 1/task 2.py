# Task - 2 Number Guessing Game


import customtkinter as ctk
import time
import random

app = ctk.CTk()
app._set_appearance_mode("dark")
app.resizable(width=False,height=False)
ctk.set_appearance_mode('dark')

app.geometry("500x550")


class Main:
    def __init__(self):
        self.main_frame = ctk.CTkFrame(master=app, corner_radius=10 , bg_color="transparent")
        self.main_label = ctk.CTkLabel(master=self.main_frame,text=" |  Guess the Number  | ", font=("Bowlby" , 20) ,  corner_radius=80 , anchor="center" , bg_color="transparent") 
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
        message1 = """Thank you for choosing to play the Number Guessing Game! We are committed to protecting your privacy and ensuring your experience is safe and enjoyable. This privacy policy explains how we collect, use, and safeguard your information when you use our app.

1. Information We Collect

The Number Guessing Game does not collect any personal information from users. The app only processes the game data, which includes:

Your guesses
Game progress (i.e., number of attempts)
    
2. Use of Data

All data processed within the app is used solely for the gameplay experience and is not transmitted to any external servers or third parties.

3. Data Security

We value your trust in providing us with your game data, and we strive to use commercially acceptable means toprotect it. However, remember that no method of transmission over the internet or method of electronic storageis 100% secure and reliable, and we cannot guarantee its absolute security.

4. Third-Party Services

The Number Guessing Game does not use third-party services that collect or track user data."""


        self.text_box.insert(ctk.END,message1)
        self.text_box.configure(state = "disabled" )



    def show_main_screen(self):
        self.main_frame.pack()
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
        start.start_frame.pack()
        start.start_button_frame.pack()


class Start:
    def __init__(self):
        self.start_frame = ctk.CTkFrame(master=app ,corner_radius= 10 , bg_color="transparent")
        self.start_label = ctk.CTkLabel(master=self.start_frame ,text="How to Play ?" ,font=("Bowlby" , 20) , corner_radius=10 , anchor="center")
        self.info_box = ctk.CTkTextbox(master=self.start_frame , corner_radius=10 , width=400 , font= ("Bowlby" , 15),wrap = "word")
        self.start_button_frame = ctk.CTkFrame(master=app , corner_radius=10)
        self.start_button = ctk.CTkButton(master=self.start_button_frame , text="Start" , corner_radius=10 , command=lambda:self.hide_all() or self.move_game_screen())
        self.back_button = ctk.CTkButton(master=self.start_button_frame , text="Back" , corner_radius=10,command=lambda:self.show_back_screen())

    def show_start_page(self):
        self.start_frame.pack(pady = 10 , fill = "both")
        self.start_label.pack(pady = 10)
        info_message = """
You guess the number and write into textbox. The computer will check if it matches the output. 

If you guessed correctly, you'll win. Otherwise , You Lose."""
        self.info_box.pack(pady = 10 ,expand = True)
        self.info_box.insert(ctk.END , info_message)
        self.info_box.configure(state = "disabled")
        self.start_button_frame.pack(fill = "x"  , pady = 25)
        self.back_button.pack(side = "left" , padx = 60)
        self.start_button.pack(side = "right", padx = 70)


    def show_back_screen(self):
        self.start_frame.pack_forget()
        self.start_button_frame.pack_forget()
        main.show_main_screen()

    def hide_start_screen(self):
        self.start_button_frame.pack_forget()
        self.start_button.pack_forget()
        self.back_button.pack_forget()
        self.start_label.pack_forget()
        self.start_frame.pack_forget()
        

        app.after(100 , self.move_game_screen)

        

    def hide_all(self):
        # flag = True
        self.start_frame.pack_forget()
        self.start_button_frame.pack_forget()
        main.main_frame.pack_forget()
        main.main_button_frame.pack_forget()
        # return flag
    
    def move_game_screen(self):
        game = Game()
        game.show_game_window()


  
class Game:

    def __init__(self):

        self.game_frame = ctk.CTkFrame(master=app ,corner_radius= 10 , bg_color="transparent")
        self.main_label = ctk.CTkLabel(master=app ,text="Guess The Number ?" ,font=("Bowlby" , 20) , corner_radius=10 , anchor="center")
        self.loading_bar = ctk.CTkProgressBar(master=self.game_frame , corner_radius=10,bg_color="transparent")
        self.loading_label = ctk.CTkLabel(master=app , text="Creating guesses... Please wait. ")

        self.loading_bar.set(0)

#Game Screen
        self.white_frame = ctk.CTkFrame(master=app , corner_radius=10 , width=200 , height=200)
        self.label = ctk.CTkLabel(master=self.white_frame , corner_radius=10 , text="Enter the number : " , anchor="center")
        self.hint = ctk.CTkLabel(master=app , anchor="s" , text="Note: Number lies between 1 - 999. Guess Carefully !")
        self.entry_box = ctk.CTkEntry(master=self.white_frame , corner_radius=10 , placeholder_text="e.g 123")
        self.guess_button = ctk.CTkButton(master=self.white_frame , corner_radius=20 , text="Guess" , anchor="center" , command=lambda:self.guess_the_number())

        self.warning1 = ctk.CTkLabel(master=self.white_frame , corner_radius= 10 , text="Enter number please!" , anchor='center')

        self.warning2 = ctk.CTkLabel(master=self.white_frame , corner_radius= 10 , text="Note: No more than 3 digits !" , anchor='center')

        self.correct_guess = ctk.CTkLabel(master=self.white_frame , text="You guessed correctly ! \n Congrats" , text_color="#39e75f" , corner_radius=10 , anchor="center")
        
        self.wrong_guess = ctk.CTkLabel(master=self.white_frame , text="Wrong Guess ! \n Try Again !" , text_color="#ff0000" , corner_radius=10 , anchor="center")

        self.try_button = ctk.CTkButton(master=self.white_frame , corner_radius=20 , text="Try Again" , anchor="center" , command=lambda:self.try_again())

    def run_loading_animation(self):
        for i in range(0 , 101 , 10):
            self.loading_bar.set(i/100)
            app.update()
            time.sleep(0.1)
        self.loading_bar.pack_forget()
        self.loading_label.pack_forget()



    def guess_the_number(self):
            # self.warning.pack_forget()
        self.entered_number = str(self.entry_box.get())
        self.entered_number = self.entered_number.strip()
        print(f"Entered number : {self.entered_number}\n")
        
        if self.entered_number == "" or None:
            self.warning1.pack()
            self.correct_guess.pack_forget()
            self.wrong_guess.pack_forget()
            # self

    
        else:
            self.warning1.pack_forget()
            # app.update()

            a = 0
            b = 999
            self.length_of_number = len(self.entered_number)
            self.guessed_number = "612"
            print(f"The size of number is : {self.length_of_number}\n")
            
            if(self.length_of_number <=3) and (self.entered_number == self.guessed_number):
                print(f"The guessed number is : {self.guessed_number}")
                print("The number you entered : ",self.entered_number)
                self.correct_guess.pack(pady =10)
            else:
                self.correct_guess.pack_forget()

            if (self.entered_number != self.guessed_number) or (self.length_of_number<len(self.guessed_number)):
                self.wrong_guess.pack(pady = 10)
                self.try_button.pack(pady = 10)
            else:
                self.wrong_guess.pack_forget()
                self.try_button.pack_forget()


    def try_again(self):
        app.destroy()


    def show_game_window(self):
        self.game_frame.pack(fill = "both")
        self.main_label.pack(pady = 10)
        self.loading_label.pack(pady = 10)
        self.loading_bar.pack(pady = 10 , fill = 'both' , side = "bottom")
        app.after(50 , self.run_loading_animation)

        self.white_frame.pack(pady = 20)
        self.label.pack(pady = 10)
        self.entry_box.pack(pady = 10)
        self.guess_button.pack(pady = 10)
        self.hint.pack(pady = 10)


main = Main()
if main.show_main_screen():
    main.hide_main_page()
    main.main_button_frame.pack_forget()

start = Start()

if start.show_start_page():
    start.hide_start_screen()
    print("Start Screen is hidden now..")

    game = Game()
    game.show_game_window()
    game.guess_the_number()
   

app.mainloop()
