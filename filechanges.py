import os

contents = os.listdir(r"/workspaces/Python-Programming/")
[print(f" - {file}") for file in contents]
