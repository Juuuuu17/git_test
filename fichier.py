import re

# Open the file and read its contents
with open('text.txt', 'r') as f:
    text = f.read()

# Use the findall() method to find all occurrences of the regex
matches = re.findall(r'luck[a-z]*', text)

# Print the matches
print(matches)