import webbrowser
import sys

base_url = "https://automatetheboringstuff.com/2e/chapter" 
chapter = sys.argv[1]
full_url = f"{base_url}{chapter}"

print(full_url)

webbrowser.open(full_url)
