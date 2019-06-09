import time
from PIL import Image, ImageDraw, ImageFont
#import epd7in5 # <-- uncomment for actual runtime
#epd = epd7in5.EPD() # <-- uncomment for actual runtime

def draw_text():
    debug = 1 # <-- switch this to a 1 to turn debug mode on
    line = 20
    while True:
        if debug == 0:
            epd.init() # Initialize sign if debug mode is off
        time.sleep(2)
        # Create the blank background file
        img = Image.new('RGB', (640, 384), color = 'white')

        draw = ImageDraw.Draw(img)
        
        # create the ImageFont instance
        font = ImageFont.truetype('fonts/clan-book-webfont.ttf', 200)
        
        line_height = font.getsize('hg')[1]

        hourText = "Hr " + str(line)

        draw.text((10, 10), hourText, fill='black', font=font)
        draw.text((10, 180), str(time.strftime("%H:%M")), fill='black', font=font)
        img.save("currentHour.png")
        if debug == 1:
            img.show() #Show image instead of pushing to sign if debug mode
            time.sleep(3) # Sleep for 3 seconds
        else:
            epd.display_frame(epd.get_frame_buffer(img))
            time.sleep(60*60) # Sleep for 1 hour
        line += 1 #Iterate line for next hour and re-start loop

        #epd.display_frame(epd.get_frame_buffer(img))
        #img.show() # <-- Debugging
        #print("Debug: send image to frame here.")
        #epd.display_frame(epd.get_frame_buffer(img))

draw_text()
