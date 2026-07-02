import re

txt = "The rain in Spain"

# Evaluates the pattern and returns a Match object if successful
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
    print(f"Matched text: {x.group()}")
    print(f"Character span: {x.span()}")
else:
    print("No match")

