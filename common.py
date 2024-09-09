from datetime import datetime


def changeLog(t):
    with open("log", 'r') as f:
        lines = f.read()
    with open("log", "w") as f:
        f.write(f"{datetime.now().strftime("%H:%M:%S")}:  {t}\n{lines}")


def changeLink(t):
    with open("link", 'w') as f:
        f.write(t)
