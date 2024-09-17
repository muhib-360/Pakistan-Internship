#Task 3 - Text Based Adventure Game
import time
import pygame

class Main:
    def __init__(self):
        head = ("WELCOME TO ADVENTURE ROOMS\n")
        print(head.center(150))
        self.agree = self.createworld()
        # self.disagree = self.destroyworld()
        self.credits = "This is created by me...".center(200)
        print(self.credits)
        
        self.createaccount = "Create an account now ! \n Sign In || Sign Up"
        print(self.createaccount)
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.4)





    def createworld(self):
        text = ("This world is temporary yet a good place to live and enjoy !")
        time.sleep(0.5)
        print(text.center(150))

        ask_user = input("Do you agree or not ? Y/N -->  ").lower()

        if ask_user == "y":
            self.build_rooms()

        ask_room = input("Which room you want to go ?").lower().strip()
        ask_room = "".join(ask_room.split())

        if ask_room == "room1":
            self.Room1()


    def build_rooms(self):
        time.sleep(1), print("Building Rooms for You ! ")
        self.available_rooms = """
        Room 1 : Music
        Room 2 : Games
        Room 3 : Tech
        """
        print(self.available_rooms)

    def Room1(self):
        
        room1 = """Currently, these songs are trending on Spotify.
        

        1) Anuv Jain - Jo Tum Mere Ho
        2) Maanu - Jhol (w/ Annural Khalid)
        3) Faheem Abdullah - Ishq (w/ Rauhan Malik)
        4) AP Dhillon - Old Money
        5) Anuv Jain - Husn\n"""

        print(room1)

        self.play_music = input("I want to play song (1-5) : ")
        time.sleep(0.3)
        print(f"Playing music : {self.play_music}")
        self.stop_music = input("Enter quit to stop music. Else ignore this message").lower()
        while self.stop_music !="quit" and self.stop_music !="":
            if self.play_music == '1':
                pygame.mixer.music.load("/music/1.mp3")
                pygame.mixer.music.play()
            elif self.play_music == '2':
                pygame.mixer.music.load("/music/2.mp3")
                pygame.mixer.music.play()
            elif self.play_music == '3':
                pygame.mixer.music.load("/music/3.mp3")
                pygame.mixer.music.play()
            elif self.play_music == '4':
                pygame.mixer.music.load("/music/4.mp3")            
                pygame.mixer.music.play()
            elif self.play_music == '5':
                pygame.mixer.music.load("/music/5.mp3")
                pygame.mixer.music.play()

            else:
                print("Invalid Input | Try Again ")
        
        time.sleep(0.3)
        pygame.mixer.music.stop()
        print("Music is stopped by the user.")


testing = Main()
testing.createworld()







