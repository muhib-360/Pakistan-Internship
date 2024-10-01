import time
import os
import shutil

class Main:
    def __init__(self):
        print(" | Welcome to Automated File Organizer | ".center(150))
        print("where you can organize your files perfectly !\n".center(150))

    def take_dir_path(self):
        while True:
            self.ask_user = input("Enter the directory path: ").lower()
            if not os.path.isdir(self.ask_user):
                print("Not a directory...\nTry Again!\n")
                continue
            else:
                print("Searching directories 🔍")
                time.sleep(0.3)
                print("Directory path found ✔")
                break

    def check_for_images(self):
        image_count = 0
        self.image_formats = ['tiff', 'jpeg', 'img', 'png', 'jpg']
        take_path = self.ask_user

        for root, dirs, files in os.walk(take_path):
            for file in files:
                if self.is_it_image(file):
                    image_count += 1
        print(f"{image_count} Images Found \n")
        return image_count > 0

    def check_for_docs(self):
        doc_count = 0
        self.doc_formats = ['docx', 'xml', 'pdf', 'ppt', 'csv']
        take_path = self.ask_user

        for root, dirs, files in os.walk(take_path):
            for file in files:
                if self.is_it_doc(file):
                    doc_count += 1
        print(f"{doc_count} Documents Found \n")
        return doc_count > 0

    def condition(self):
        if self.check_for_images():
            for root, dirs, files in os.walk(self.ask_user):
                for file in files:
                    if self.is_it_image(file):
                        file_path = os.path.join(root, file)
                        if not self.check_images_folder(root):
                            os.mkdir(os.path.join(root, "Images"))
                        print("Moving images to folder....")
                        time.sleep(0.4)
                        shutil.move(file_path, os.path.join(root, "Images"))

        else:
            print("No images to move...")

        if self.check_for_docs():
            for root, dirs, files in os.walk(self.ask_user):
                for file in files:
                    if self.is_it_doc(file):
                        file_path = os.path.join(root, file)
                        if not self.check_doc_folder(root):
                            os.mkdir(os.path.join(root, "Documents"))
                        print("Moving docs to folder....")
                        time.sleep(0.4)
                        shutil.move(file_path, os.path.join(root, "Documents"))
        else:
            print("No documents to move...")

    def check_doc_folder(self, root):
        return "documents" in [d.lower() for d in os.listdir(root)]

    def check_images_folder(self, root):
        return "images" in [d.lower() for d in os.listdir(root)]

    def is_it_image(self, file):
        return file.lower().endswith(tuple(self.image_formats))

    def is_it_doc(self, file):
        return file.lower().endswith(tuple(self.doc_formats))


testing = Main()
testing.take_dir_path()
testing.condition()
