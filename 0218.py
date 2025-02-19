def abc(level):
    if level == 2:
        return

    for i in range(2):
        abc(level+1)