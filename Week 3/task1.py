# Task 1 : Text File Analyzer

from collections import Counter
import time

class Main:
    def __init__(self):
        print(" | Welcome to Text File Analyzer | ".center(150))

    def take_file(self):
        while True:

            print("Taking path from directory....\n")

            time.sleep(0.3)

            self.file_path = "test.txt"
            if not self.file_path[-4:] ==".txt":
                print("File format must be in '.txt' \n")
                break
            return

    def word_count(self):
        count = 0
        with open(self.file_path , 'r') as file:
            data = file.read()
            print(f"Text Data : {data}\n")

            lines = data.split()
            count +=len(lines)  
            print(f"Word Count : {count}")
                
    def common_word(self):
        with open(self.file_path , 'r') as file:
            data = file.read().lower()

            words = data.split()

            word_counts = Counter(words)

            common_word = word_counts.most_common(1)[0]

            print(f"Most common word :  {common_word[0]}")
            print(f"No of occurences : {common_word[1]}")

    def line_count(self):
        with open(self.file_path , 'r') as file:
            data = file.readlines()

            line_count = len(data)

            print(f"Line Count : {line_count}")


testing = Main()
testing.take_file()
testing.word_count()
testing.common_word()
testing.line_count()



