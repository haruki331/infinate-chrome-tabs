import webbrowser, random
def openbook():
    randomnumber = random.randint(100000,999999)
    webbrowser.open('https://nhentai.net/g/'+ str(randomnumber))
while True:
    openbook()
