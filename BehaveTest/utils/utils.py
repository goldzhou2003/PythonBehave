import os

def log(message):
    with open('./log.txt', 'a') as f:
        f.write(message)
        f.write(os.linesep)
        f.flush()
