import webbrowser
import sys

base_url = "https://handbook.unimelb.edu.au/2021/subjects/" 
subject = sys.argv[1]
full_url = f"{base_url}{subject}"

print(full_url)

webbrowser.open(full_url)