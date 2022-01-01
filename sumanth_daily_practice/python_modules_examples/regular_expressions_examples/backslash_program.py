# metacharacters = ^,[],\,.,{},(),?,*,+,|,$

import re

a = "Sumanth.Mahesh"



match = re.search(r".", a)

print(match)

match = re.search(r"\.", a)

print(match)
