from PIL import Image, PSDraw

im = Image.open("1.png")
title = "Hi there!"
box = (1 * 72, 2 * 72, 7 * 72, 10 * 72)

ps = PSDraw.PSDraw()  # default is sys.stdout
ps.begin_document(title)

# draw title
ps.setfont("HelveticaNarrow-Bold", 36)
ps.text((3 * 72, 4 * 72), title)

ps.end_document()
