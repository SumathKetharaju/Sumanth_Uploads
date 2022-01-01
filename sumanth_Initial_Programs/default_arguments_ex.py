def banner(message, border='_'):

    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("super star")
banner("mahesh babu is a super star", "*")
banner("mahesh babu is a super star", border="*")
banner(border='.', message = "he is one of top heros")
banner("super star")