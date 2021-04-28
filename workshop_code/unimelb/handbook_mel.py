# CC0 1.0 Universal - Harsh Deep
# This program takes the name of a unimelb course and opens the browser there.

import webbrowser
import sys

base_url = "" 
subject = sys.argv[1]
full_url = f"{base_url}{subject}"

print(full_url)

webbrowser.open(full_url)