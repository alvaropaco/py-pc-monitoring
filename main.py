from datetime import datetime
from pynput import mouse
from store import Store

# Connection URL
url = 'https://8b6a2180-4759-4464-9d7d-cb02cd512c19-bluemix:112fc643a14a9ea5c38732cd5abdf95d3ff40bd8bf15db73107d8089069b38fa@8b6a2180-4759-4464-9d7d-cb02cd512c19-bluemix.cloudant.com'

file = open("testfile.txt","w") 

startAt = now = datetime.now()
currentDateTime = datetime.now()

def on_move(x, y):
    currentDateTime = datetime.now()
    strAt = '{0} to {1}\n'.format(startAt, currentDateTime)
    # print(strAt)
    file.write(strAt)

def on_click(x, y, button, pressed):
    strAt = 'Pointer moved to {0} at {1}\n'.format(
        (x, y), currentDateTime)
    file.write(strAt)
    if not pressed:
        # Stop listener
        return True

def on_scroll(x, y, dx, dy):
    currentDateTime = datetime.now()
    strAt = 'Scrolled {0} to {1} at {2}'.format(
        'down' if dy < 0 else 'up',
        (x, y), currentDateTime)
    
    store.save({'datetime': currentDateTime})
    # file.write(strAt)
    # print('Scrolled {0} to {1} at {2}'.format(
    #     'down' if dy < 0 else 'up',
    #     (x, y), currentDateTime))

def main():
    # Collect events until released
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()

def connect(hostURL, db):
    return Store(hostURL, db)

if __name__== "__main__":
    store = connect(url, 'monitor')
    main()