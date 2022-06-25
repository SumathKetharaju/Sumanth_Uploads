import re
# valid_gamil = "sumanth.@$-_K123@gmail.com"
# valid_gamil = "suma45nth.@$@-_K123sumanth@gmail.com"
# valid_gamil = "sumanth@gmail.com"
# valid_gamil = "sumanth568@gmail.com"
# valid_gamil = "sumanth.l@gmail.com"
# valid_gamil = "sumanth_j693@gmail.com"
valid_gamil = "sumanth.ketharaju243@gmail.com"
# valid_gamil = "Hello1@gmail.com"
# valid_gamil = "hello~@gmail.com"
# valid_gamil = "hello@gmail.world"
# valid_gamil = "hello_world@gmail.com"
# valid_gamil = "hello_world@hotmail.com"
# valid_gamil = "hello_world@gmail.co.in"

# gmail_pattern = re.compile(r"^[A-Za-z][\w]+(\.|@|\$|-|_)*[\w+]*[@]+gmail\.com$")
gmail_pattern = re.compile(r"^[A-Za-z][\w]+(\.|@|\$|-|_|~)*[\w+]*[@]+[a-z]{1,9}\.([a-z]{1,5}\.)*[a-z]{1,5}$")
gmail_match = gmail_pattern.search(valid_gamil)
print(gmail_match)
if gmail_match:
    print(f"'{gmail_match.group()}' is a valid gmail")
else:
    print("Not a valid gmail")
