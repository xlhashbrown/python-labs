# Program 21: deleting files

import os

if os.path.isfile("log_old.txt"):
    os.remove("log_old.txt")
    print("log_old.txt has been deleted.")
else:
    print("log_old.txt was not found.")
