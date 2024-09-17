#Task 3 - Text Based Adventure Game
import time
import pygame

class Main:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.4)
        head = ("WELCOME TO ADVENTURE ROOMS\n")
        print(head.center(150))
        self.agree = self.createworld()
        print(self.credits)
        self.disagree = self.destroy_world()
        print(self.credits)
        self.credits = "This is created by me...".center(200)
        
        self.createaccount = "Create an account now ! \n Sign In || Sign Up"
        print(self.createaccount)


    def createworld(self):
        text = ("This world is temporary yet a good place to live and enjoy !")
        time.sleep(0.5)
        print(text.center(150))

        ask_user = input("Do you agree or not ? Yes/No -->  \n").lower()
        while True:

            if ask_user == "n" or ask_user =="no":
                self.destroy_world()

            if ask_user == "y" or ask_user =="yes":
                if self.build_rooms():
                    break


            ask_room = input("Which room you want to go ?").lower().strip()
            ask_room = "".join(ask_room.split())

            if ask_room == "room1":
                self.Room1()

            if ask_room =="room2":
                self.Room2()

            if ask_room =="room3":
                self.Room3()


    def build_rooms(self):
        time.sleep(0.4), print("Building Rooms for You ! ")
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

        while True:
            self.play_music = input("I want to play song (1-5) : ")
            
            if self.play_music == '1':
                pygame.mixer.music.load("music/1.mp3")
                pygame.mixer.music.play()
            elif self.play_music == '2':
                pygame.mixer.music.load("music/2.mp3")
                pygame.mixer.music.play()
            elif self.play_music == '3':
                pygame.mixer.music.load("music/3.mp3")
                pygame.mixer.music.play()
            elif self.play_music == '4':
                pygame.mixer.music.load("music/4.mp3")
                pygame.mixer.music.play()
            elif self.play_music == '5':
                pygame.mixer.music.load("music/5.mp3")
                pygame.mixer.music.play()
            else:
                print("Invalid Input | Try Again !")
                continue

            time.sleep(0.3)
            print(f"Playing music : {self.play_music}")
            
            self.stop_music = input("Enter 'quit' to stop music. Else, ignore this message: ").lower()
            if self.stop_music == "quit":
                pygame.mixer.music.stop()
                print("Music is stopped by the user.")
                break

    def Room2(self):
        room2 = "Gaming is a popular form of entertainment that combines interactive experiences with digital storytelling. It spans a wide range of genres, from action-packed adventures to strategy-based puzzles, offering players immersive environments and challenges. With advancements in technology, gaming has evolved into a social platform, where players from around the world can connect, compete, and collaborate. Beyond entertainment, gaming has also found its place in education, virtual reality, and professional esports, making it a versatile and ever-growing industry.\n"

        print(room2)
        flag = True

        while flag:
            ask_user = input("Are you interested in gaming ?  Y/N").lower()

            if ask_user =='n' or ask_user == "no":
                print("means you are interested in something else..")
                break

            if ask_user =='y' or ask_user =="yes":
                steam_games = """These games are most played on Steam platform. Look out the ratings !\n
                1) Counter-Strike 2                 Current Score: 1,303,201
                2) DOTA 2                           Current Score: 668,201
                3) Apex Legends                     Current Score: 624,629 
                4) PUBG: BATTLEGROUNDS              Current Score: 616,782
                5) CyberPUNK 2077                   Current Score: 598,235\n"""

                print(steam_games)

            ask_likings = input("Do you want to know minimum specification required for these games ?  Y/N" ).lower()

            if ask_likings =='y' or ask_likings == "yes":
                min_specs = """
1. Counter-Strike 2
OS: Windows 10 (64-bit)
Processor: Intel Core i3-6100 / AMD Ryzen 3 1200
Memory: 6 GB RAM
Graphics: NVIDIA GeForce GTX 1050 / AMD Radeon R7 450
DirectX: Version 11
Storage: 15 GB available space \n
2. DOTA 2
OS: Windows 7 or newer
Processor: Intel Core 2 Duo 2.8 GHz / AMD Athlon 64 X2 4400+
Memory: 4 GB RAM
Graphics: NVIDIA GeForce 8600/9600GT / ATI/AMD Radeon HD2600/3600
DirectX: Version 9.0c
Storage: 15 GB available space\n
3. Apex Legends
OS: Windows 7 64-bit
Processor: Intel Core i3-6300 3.8 GHz / AMD Ryzen 5 3550U
Memory: 8 GB RAM
Graphics: NVIDIA GeForce GT 640 / AMD Radeon HD 7730
DirectX: Version 11
Storage: 22 GB available space\n
4. PUBG Battlegrounds
OS: Windows 10 64-bit
Processor: Intel Core i5-4430 / AMD Ryzen 3 1200
Memory: 8 GB RAM
Graphics: NVIDIA GeForce GTX 960 / AMD Radeon R7 370
DirectX: Version 11
Storage: 30 GB available space\n
5. Cyberpunk 2077
OS: Windows 10 (64-bit)
Processor: Intel Core i5-3570K / AMD Ryzen 3 3200G
Memory: 8 GB RAM
Graphics: NVIDIA GeForce GTX 780 / AMD Radeon RX 470
DirectX: Version 12
Storage: 70 GB available space\n"""

            print(min_specs)
            if ask_likings =='n' or ask_likings == "no":
                print("Taking back to the home screen...\n")
                time.sleep(0.3)
                flag = False
                break 
        

    def Room3(self):
        pygame.mixer.music.load("music/tech.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()

        print("Welcome to the room of Technology, where we share latest news and happenings in the tech world.")

        while True:
            ask_user = input("Are you interested in tech news ?  \n or take me back to home screen  (Y/N) \n").lower()

            if ask_user =="y":
                tech_news = """
Apple Vision Pro: Apple's Vision Pro headset, priced around $4,000, is set to make waves with its advanced augmented reality and virtual reality capabilities. The launch in 2024 is highly anticipated, with expectations that it may lead to more affordable versions in the future​(TechRadar).

Foldable Phones: Companies like Samsung, Google, and Motorola continue to innovate with foldable devices. The next iterations, such as the Samsung Galaxy Z Fold 6, are expected to be lighter and more compact​(TechRadar).

Quantum Computing: Researchers recently discovered a one-dimensional topological insulator, a breakthrough that could have significant implications for quantum computing and energy efficiency in devices​(SciTech Daily).
"""
                print(tech_news)

            if ask_user =="n":
                print("Coming back to the main screen...")
                time.sleep(0.5)
                break

    def destroy_world(self):
        pygame.mixer.music.load("music/sad.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()


        print("This clearly shows you have no interest living in this world.")
        time.sleep(0.4)
        eng_quotes = ["Here are some english quotes for you : \n Emotional pain is not something that should be hidden away and never spoken about. There is truth in your pain, there is growth in your pain, but only if it’s first brought out into the open.” — Steven Aitchison" ,
        "The advice I’d give to somebody that’s silently struggling is, you don’t have to live that way. You don’t have to struggle in silence. You can be un-silent. — Demi Lovato" ,
        "Talk to yourself like you would to someone you love.” — Brené Brown" ,
        "One small crack does not mean that you are broken, it means that you were put to the test and you didn’t fall apart.” — Linda Poindexter"]

        urdu_quotes = ["Here are some urdu quotes for you !\n Jab zindagi mushkil ho jaye to yeh mat bhoolo ke har raat ke baad aik roshan subah aati hai.",
        "Apni mushkilat ko apni taqat banao, kyunke har zakham aik sabaq deta hai." ,
        "Kabhi kabhi haarna bhi jeetne ke barabar hota hai, kyunke yeh humein agay barhne ka rasta dikhata hai."]

        while True:
            ask_user = input("Do you need some mental or emotional support ?  Y/N").lower()
            if ask_user =="n" or ask_user =="no":
                print("Considering your mental condition, I would suggest you to go for medical assisstance. This will really help you to comfort you anxity or stress.\n")
                time.sleep(0.3)
                print("Thank you for saving my time..\n")
                break
            ask_lang = input("Quotes in English or Urdu ? (Eng/Urd)\n").lower()
            
            if (ask_user == "y" or ask_user =="yes") and (ask_lang == "eng" or ask_lang =="english"):
                for quote in eng_quotes:
                    print(f"{quote}\n")
                    time.sleep(0.5)
            if (ask_user =="y" or ask_user =="yes") and (ask_lang =="urd" or ask_lang == "urdu"):
                for quote in urdu_quotes:
                    print(f"{quote}\n")
                    time.sleep(0.4)

testing = Main()
testing.createworld()







