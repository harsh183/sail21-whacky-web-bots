import webbrowser
import sys

base_url = "https://courses.illinois.edu/schedule/DEFAULT/DEFAULT" 
subject = sys.argv[1]
number = sys.argv[2]
full_url = f"{base_url}/{subject}/{number}"

print(full_url)

webbrowser.open(full_url)


