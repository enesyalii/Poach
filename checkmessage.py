from bans import badword
swears = ['Fuck']
def checkmsg(message):
    for swear in swears:
        if swear in message.content.lower():
            print("Found bad word")
            badword(message.author)