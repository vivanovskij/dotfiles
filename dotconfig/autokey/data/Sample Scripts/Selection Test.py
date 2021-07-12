text = clipboard.get_selection()
keyboard.send_key("<delete>")
keyboard.send_keys("text The %s was here previously" % text)