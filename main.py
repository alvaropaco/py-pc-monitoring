from datetime import datetime
from pynput import mouse
from store import Store
from uuid import getnode as get_mac

# Connection URL
url = 'https://8b6a2180-4759-4464-9d7d-cb02cd512c19-bluemix:112fc643a14a9ea5c38732cd5abdf95d3ff40bd8bf15db73107d8089069b38fa@8b6a2180-4759-4464-9d7d-cb02cd512c19-bluemix.cloudant.com'

file = open("testfile.txt","w") 

startAt = datetime.now()
me = get_mac()
currentDateTime = datetime.now()

def on_move(x, y):
    currentDateTime = datetime.now()
    record = {
        'startedAt': str(startAt),
        'datetime': str(currentDateTime),
        'MACaddr' : me
    }
    doc_id, doc_rev = store.save(record)
    print(record)

def on_click(x, y, button, pressed):
    currentDateTime = datetime.now()
    doc_id, doc_rev = store.save({
        'startedAt': str(startAt),
        'datetime': str(currentDateTime),
        'MACaddr' : me
    })
    if not pressed:
        # Stop listener
        return True

def on_scroll(x, y, dx, dy):
    currentDateTime = datetime.now()
    doc_id, doc_rev = store.save({
        'startedAt': str(startAt),
        'datetime': str(currentDateTime),
        'MACaddr' : me
    })

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