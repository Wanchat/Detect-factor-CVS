from PIL import ImageFont, ImageDraw, Image
import numpy as np

fontpath = "data/Prompt-Regular.ttf"

def text(frame, roi, text, size, color):
    font = ImageFont.truetype(fontpath, size)
    ascent, descent = font.getmetrics()
    (width, baseline), (offset_x, offset_y) = font.font.getsize(text)

    img_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(img_pil,  "RGBA")

    draw.rectangle(((roi[0], roi[1]+(offset_y-2)), 
    	               (roi[0]+width, roi[1]+descent+baseline)), 
    	               fill=(255,255,255,100))

    draw.text(roi, "{}".format(text), font=font, fill=color)

    return  np.array(img_pil)

