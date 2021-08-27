#!/usr/bin/env python3
import os
import time

from lib.waveshare_epd import epd7in5_V2

from PIL import Image, ImageDraw, ImageFont

pic_dir = 'pic'

def initialize():
  try:
    display = epd7in5_V2.EPD()
    display.init()
    display.Clear()

    # Done to support landscape mode
    w = display.width
    h = display.height

    while True:
      display_loop(display,w,h)
      time.sleep(5)

  except IOError as e:
    print(e)


def display_loop(display,w,h):

  body = ImageFont.truetype('font/Roboto-Regular.ttf', 24, index=0)
  image = Image.new(mode='1', size=(w,h), color=255)
  draw = ImageDraw.Draw(image)

  draw.text((0,0), 'Hello Robbyn this is the beginning of the home board.', font = body, fill=0, align='left')
  print('writing image')
  display.display(display.getbuffer(image)) 


def main():
  initialize()


if __name__ == '__main__':
  main()
