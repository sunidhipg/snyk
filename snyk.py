import os
user_input = input("Enter a command: ")
os.system(user_input)  # ⚠️ This is dangerous if unsanitized
