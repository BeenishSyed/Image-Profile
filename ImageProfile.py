# ****Rose colored glasses****
def roseColoredGlasses(mypic):
  mypic = get_pic()
  pixels = getPixels(mypic)
  r2 = 255
  g2 = 174
  b2 = 201
  for i in pixels:
    r1 = getRed(i)
    g1 = getGreen(i) 
    b1 = getBlue(i)
    setRed(i,.4*r1+.6*r2)
    setGreen(i,0.4*g1+.6*g2)
    setBlue(i,0.4*b1+.6*b2)   
  show(mypic)
  
# **** Make Negative Image ****
def makeNegative(mypic):
  #mypic = get_pic()
  pixels = getPixels(mypic)

  for p in pixels:
    r = getRed(p)
    setRed(p, abs(r - 255))
    s = getBlue(p)
    setBlue(p, abs(s - 255))
    t = getGreen(p)
    setGreen(p, abs(t - 255))
  show(mypic)
  
  # **** Make a picture better black and white***
  def betterBnW(mypic):
  pixels = getPixels(mypic)
  for p in pixels:
    r = getRed(p)      
    r = r*0.299 #Weight the red value
    
    g = getGreen(p)
    g = g*0.587 #Weight the green value
    
    b = getBlue(p)
    b = b*0.114 #Weight the blue value
    
    luminance = (r+g+b) #Find luminance of the weighted red, green    
    #and blue values.
    setRed(p, luminance) 
    setGreen(p, luminance)
    setBlue(p, luminance)
  show(mypic)
  
  # **** Mirror an image bottom to top ****
  def mirrorBottomtoTop():
  pic=makePicture(path+ "\\P-antheon.jpg")
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(width):
    for y in range(height/2, height):
      pix = getPixel(pic, x, y)
      color = getColor(pix)
      newPix= getPixel(pic, x, height-y-1)
      setColor(newPix, color)
  repaint(pic)
  show(pic)
  
  #*** Shrink an image to half its width and height***
  def shrink(): 
  picture=makePicture(path + "\\P-antheon.jpg")
  oldHeight = getHeight(picture)
  oldWidth = getWidth(picture)
  newHeight = oldHeight/2 +1 # +1 to make up for odd number
  newWidth = oldWidth/2 +1 #+1 to make up for odd number
  
  newPicture = makeEmptyPicture(newWidth, newHeight)
  xPos=0
  
  for x in range (0, oldWidth, 2):
    yPos=0
    for y in range (0, oldHeight, 2):
      pixel = getPixel(picture, x , y)
      color = getColor(pixel)
      newPixel = getPixel(newPicture, xPos, yPos) 
      setColor(newPixel, color)
      yPos=yPos+1
    xPos=xPos+1
  repaint(newPicture)
  writePictureTo(newPicture,out_path + "//shrinkPic.jpg")
  show(newPicture)
  
  # **** make collage using all the functions***
  def betterBnW (picture):
  pixels=getPixels(picture)
  for i in pixels:
    R = getRed(i)* 0.299
    G = getGreen(i)*0.587
    B = getBlue (i)*0.114
    average = R+G+B
    newColor = makeColor(average, average, average)
    setColor(i, newColor)
  return picture
 
def makeNegative(mypic):
  pixels = getPixels(mypic)
  for p in pixels:
    r = getRed(p)
    setRed(p, abs(r - 255))
    s = getBlue(p)
    setBlue(p, abs(s - 255))
    t = getGreen(p)
    setGreen(p, abs(t - 255))
  return mypic
  

def pyCopy(source, target, targetX, targetY):
  width = getWidth(source)
  height = getHeight(source)
  for x in range (width):
    for y in range (height):
      pixel = getPixel(source, x, y)
      color = getColor(pixel)
      newpixel = getPixel(target, x+targetX, y+targetY)
      setColor(newpixel, color)


def shrink(picture):
  oldWidth = getWidth(picture)
  oldHeight = getHeight(picture)
  newHeight = oldHeight/2 +1 # +1 to make up for odd number
  newWidth = oldWidth/2 +1 #+1 to make up for odd number
  newPicture = makeEmptyPicture(newWidth, newHeight)
  xPos=0
  for x in range (0, oldWidth, 2):
    yPos=0
    for y in range (0, oldHeight, 2):
      pixel = getPixel(picture, x , y)
      color = getColor(pixel)
      newPixel = getPixel(newPicture, xPos, yPos) 
      setColor(newPixel, color)
      yPos=yPos+1
    xPos=xPos+1
  return newPicture

def mirrorImageHorizontal(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(width):
    for y in range(height/2):
      pix = getPixel(pic, x, y)
      color = getColor (pix)
      newPix = getPixel (pic, x, height-y-1)
      setColor(newPix, color)
  return pic
  
def moreRed(percent, picture):
  pixels = getPixels(picture)
  for i in pixels:
    r = getRed(i)
    value = r + r*percent/100
    setRed(i, value)
  return picture

def lessRed(percent,picture):
  pixels=getPixels(picture)
  for i in pixels:
    r = getRed(i)
    value = r - r*percent/100
    setRed(i, value)
  return picture
  
def rotatePic(picture):
  oldHeight=getHeight(picture)
  oldWidth = getWidth (picture)
  newPicture = makeEmptyPicture(getHeight(picture), getWidth(picture)) #switching height and width for new picture
  for x in range(oldWidth):
    for y in range(oldHeight):
      oldPixel = getPixel(picture, x, y)
      color = getColor(oldPixel)
      newPixel = getPixel(newPicture, y, x)
      setColor(newPixel, color)
  return newPicture


def makeCollage():
  used_width = 0 
  used_height = 0
  total_width = 2550
  total_height = 3300
  pic1 = makePicture(path + "\\Otter.jpg")
  pic2 = makePicture(path + "\\O-ranges.jpg")
  pic3 = makePicture(path + "\\Y-ellow.jpg")
  pic4 = makePicture(path + "\\CSUMB Landscape.jpg")
  pic5 = makePicture(path + "\\P-antheon.jpg")
  pic6 = makePicture(path + "\\H-ouse.jpg")
  pic7 = makePicture(path + "\\Potriat2.jpg")
  pic8 = makePicture(path + "\\T.jpg")
  pic9 = makePicture(path + "\\N.jpg")
  targetCollage = makeEmptyPicture(total_width, total_height)
 
  pic1 = makeNegative(pic1)
  targetPosX = used_width
  targetPosY = used_height
  pyCopy(pic1, targetCollage, targetPosX, targetPosY)
  used_width = getWidth(pic1) - 133 #to overlap pic and make room for 3 pictures widthwise
  
  pic2 = betterBnW(pic2)
  targetPosX = used_width
  targetPosY = used_height
  pyCopy(pic2, targetCollage, targetPosX, targetPosY)
  used_width= used_width+getWidth(pic2)-133 #to overlap pic and make room for 3 pictures widthwise
  
  pic3 = moreRed (80 , pic3)
  targetPosX = used_width
  targetPosY = used_height
  pyCopy (pic3, targetCollage, targetPosX, targetPosY)
  used_width = 0 #reset X to zero
  used_height = getHeight(pic1)
  
  pic4 = lessRed (90, pic4)
  targetPosX = used_width
  targetPosY = used_height
  pyCopy (pic4, targetCollage, targetPosX, targetPosY)
  used_width = getWidth(pic4)-261 #to overlap pic and make room for 3 pictures widthwise
  used_height = getHeight(pic2) - 150
  
  pic5 = mirrorImageHorizontal (pic5)
  targetPosX = used_width
  targetPosY = used_height
  pyCopy(pic5, targetCollage, targetPosX, targetPosY)
  used_width = used_width + getWidth(pic5)- 261 #to overlap pic and make room for 3 pictures widthwise
  used_height = getHeight(pic3)
  
  pic6 = makeNegative(pic6)
  targetPosX= used_width
  targetPosY= used_height
  pyCopy(pic6, targetCollage, targetPosX, targetPosY)
  used_width = 0 # reset x to 0 to
  used_height = getHeight(pic1) + getHeight(pic4)
  
  targetPosX = used_width
  targetPosY = used_height
  pyCopy (pic7, targetCollage, targetPosX, targetPosY)
  used_width = used_width+ getWidth(pic7)
  used_height = getHeight(pic2)+ getHeight(pic5)-150
  
  targetPosX= used_width
  targetPosY = used_height
  pyCopy(pic8, targetCollage, targetPosX, targetPosY)
  used_width = used_width+getWidth(pic8)-10
  used_height = getHeight(pic3) + getHeight (pic6)
  
  pic8=mirrorImageHorizontal(pic8)
  targetPosX=used_width
  targetPosY=used_height
  pyCopy(pic8, targetCollage, targetPosX, targetPosY)
  used_width = 0 #reset x to 0
  used_height = getHeight(pic1)+getHeight(pic4)+getHeight(pic7)
    
  pic5=rotatePic(pic5)
  targetPosX = used_width
  targetPosY = used_height
  pyCopy(pic5, targetCollage, targetPosX, targetPosY)
  used_width = used_width+ getWidth(pic5)
  
  targetPosX = used_width
  pyCopy(pic2, targetCollage, targetPosX, targetPosY)
  used_width = used_width + getWidth(pic2)
  
  pic2 = makeNegative(pic2)
  targetPosX = used_width
  targetPosY = targetPosY + 185
  pyCopy(pic2, targetCollage, targetPosX, targetPosY)
  used_width = used_width+getWidth(pic2)-110
  
  targetPosX = used_width
  pyCopy(pic5, targetCollage, targetPosX, targetPosY)
  
  used_width = 0
  used_height = getHeight(pic1)+getHeight(pic4)+getHeight(pic7)+getHeight(pic5)
  pic3= shrink(pic3)
  targetPosX=used_width
  targetPosY = used_height - 150
  pyCopy(pic3, targetCollage, targetPosX, targetPosY)
  
  targetPosY = 3300-717
  targetPosX = used_width + getWidth(pic3)
  pyCopy(pic4, targetCollage, targetPosX, targetPosY) 
  show(targetCollage)
  writePictureTo (targetCollage, out_path + "//collage.jpg")

#Define INPUT images path
path = "C:\Users\munee_000\Documents\CST 205\Module 2\Lab5 - Beenish Syed\Original_Images"

#Define path for OUTPUT images
out_path = "C:/Users/munee_000/Documents/CST 205/Module 2/Lab5 - Beenish Syed/Generated_Images"

#My Collage takes a REALLY REALLY long time to build since my files are big but it does work 
makeCollage() 

# *** Fix Red Eye in an image****

def fixRedEye(pic):
  newcolor = makeColor(43, 29, 14)
  for x in range(183, 210):
    for y in range (280, 308):
      pixel = getPixel(pic, x, y)
      oldcolor = getColor(pixel)
      if distance (oldcolor, red) < 200:
        setColor(pixel, newcolor)
  for x in range(336, 363):
    for y in range (293, 320):
      pixel = getPixel(pic, x, y)
      oldcolor = getColor(pixel)
      if distance (oldcolor, red) < 200:
        setColor(pixel, newcolor)
        
# **** Artify an image ****
def artify(pic):
  Reds = [31,95,159,223] #Same thing as with sepia, but using fixed values instead of factors
  Greens = [31,95,159,223]
  Blues = [31,95,159,223]
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p,Reds[r//64])
    setGreen(p,Greens[g//64])
    setBlue(p,Blues[b//64])
    
    # *** Green Screen ... adds a background to a Chroma screen image***
    
    def chromaKey(picture,background):
  width = getWidth(picture)
  height = getHeight(picture)
  Green = makeColor(18,255,17)
  for x in range(0, width):
    for y in range (0, height):
      pix = getPixel(picture, x, y) #Pixel of chroma picture
      bgPixel = getPixel(background, x, y)
      checkColor = getColor(pix)
      r = getRed(pix)
      g = getGreen(pix)
      b = getBlue(pix)
      dist = distance(checkColor,Green)
      if dist < 70:
        newColor = getColor(bgPixel)
        setColor(pix, newColor)
      elif g > .8*r + .8*b:
        newColor = getColor(bgPixel)
        setColor(pix, newColor)
        
   #Make St Patrick's Day card

def negImg(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, abs(r - 255))
    s = getBlue(p)
    setBlue(p, abs(s - 255))
    t = getGreen(p)
    setGreen(p, abs(t - 255))
    return pic
    
def quadrupelMirror(pic):
  #pic=makePicture(path + "\\Samrock.jpg")
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range (width/2):
    for y in range (height):
      pix = getPixel(pic, x, y)
      colorOfPixel = getColor(pix)
      newPix = getPixel(pic, width-x-1, y) #Getting to the pixel that needs to be changed
      setColor(newPix, colorOfPixel)
  for x in range(width):
    for y in range(height/2):
      pix = getPixel(pic, x, y)
      color = getColor (pix)
      newPix = getPixel (pic, x, height-y-1)
      setColor(newPix, color)
  return pic
  

def pyCopy(source, target, targetX, targetY):
  width = getWidth(source)
  height = getHeight(source)
  for x in range (width):
    for y in range (height):
      pixel = getPixel(source, x, y)
      color = getColor(pixel)
      newpixel = getPixel(target, x+targetX, y+targetY)
      setColor(newpixel, color)
      
def makeStPatrickCard1():
  basePic = makePicture(path + "\\StPatrickBackGround.jpg")
  pic1 = makePicture(path + "\\Leprechaun1.jpg")
  pic2 = makePicture(path +"\\Leprechaun2.jpg")
  shamrockPic = makePicture(path + "\\Shamrock.jpg")
  
  basPicWidth = getWidth (basePic)
  basePicHeight = getHeight(basePic)
  
  pyCopy(pic1, basePic, 75, 75)
  targetX = getWidth(pic1)+75+50
  targetY = 75
  pyCopy(shamrockPic, basePic, targetX, targetY)
  
  shamrockPic = quadrupelMirror(shamrockPic) 
  targetX = 75
  targetY = basePicHeight - 75 - getHeight(shamrockPic)
  pyCopy(shamrockPic, basePic, targetX, targetY)
   
  targetX = targetX + getWidth(shamrockPic) + 50
  targetY = targetY-50
  pyCopy(pic2, basePic, targetX, targetY)
  
  #Write Font now
  color= makeColor(50, 158, 0)
  style = makeStyle(sansSerif, italic+bold, 55)
  addTextWithStyle(basePic, 100, 550, "Happy St Patrick's Day!", style, color)
  writePictureTo(basePic, outpath + "//StPatrickCar.jpg")
  
def makeStPatrickCard2():
  basePic = makePicture(path + "\\BaseCard.jpg")
  Logo = makePicture(path + "\\Logo1.jpg")
  horseShoe = makePicture(path +"\\HorseShoe.jpg")
  baseColor = makeColor(0,65,1) #color of the base picture taken by using explore function
  #explore(horseShoe)
  pixels = getPixels(Logo)
  #Change the white color in Logo to match the color of base picture
  for p in pixels:
    if distance(getColor(p),white)<60:
      setColor(p, baseColor)
      
  #Change the white color in horse shoe picture to match the color of base picture
  pixels = getPixels(horseShoe)
  for p in pixels:
    if distance(getColor(p),white)<100:
      setColor(p, baseColor)
      
  #Adding Logo to top left corner  
  for x in range(getWidth(Logo)):
    for y in range(getHeight(Logo)):
      pixelLogo = getPixel(Logo, x, y) #get pixel to be printed
      color = getColor(pixelLogo)
      pixelBasePic = getPixel(basePic, x, y) #get pixel to print on
      setColor(pixelBasePic, color)
  #Adding horse shoe to bottom left corner
  for x in range(getWidth(horseShoe)):
    for y in range (getHeight(horseShoe)):
      pixelHS = getPixel(horseShoe, x, y)
      z = y+ getHeight(basePic) - getHeight(horseShoe) # getting to the y position to paste horseshoe picture
      pixelBasePic = getPixel(basePic, x, z)
      setColor(pixelBasePic, getColor(pixelHS))
  #Add font now
  color = makeColor(244, 156, 50) #color similar to horseshoe color
  style = makeStyle("Freestyle Script", bold, 100)
  addTextWithStyle(basePic, int(getWidth(basePic)*0.25), int(getHeight(basePic)*.90), "Oh so Lucky!", style,color)
  writePictureTo(basePic, outpath + "//StPatrickCard2.jpg")
  repaint(basePic)
   #********* Draw Line Function***********
    def betterBnW(mypic):
  pixels = getPixels(mypic)
  for p in pixels:
    r = getRed(p)      
    r = r*0.299 #Weight the red value
    
    g = getGreen(p)
    g = g*0.587 #Weight the green value
    
    b = getBlue(p)
    b = b*0.114 #Weight the blue value
    
    luminance = (r+g+b) #Find luminance of the weighted red, green    
    #and blue values.
    setRed(p, luminance) 
    setGreen(p, luminance)
    setBlue(p, luminance)
  return mypic

def BnWLineImg(pic):
  pic = betterBnW(pic) # convert picture to black and white
  picWidth = getWidth(pic)-1
  picHeight = getHeight(pic)-1
  for x in range(picWidth):
    for y in range (picHeight):
      myPixel = getPixel(pic, x, y)
      rightPixel = getPixel(pic, x+1, y)
      bottomPixel = getPixel(pic, x, y+1)
      myPixelColor = getBlue(myPixel) # Since red green and blue have same value
      rightPixelColor = getBlue(rightPixel)
      bottomPixelColor = getBlue(bottomPixel)
      #if abs(myPixelColor - rightPixelColor)<10 and abs(myPixelColor - bottomPixelColor)<10: # makes inverted image with more black and white lines
      if abs(myPixelColor - rightPixelColor)>2 and abs(myPixelColor - bottomPixelColor)>2: # makes a sketch like image with more white and black lines
        setColor(myPixel, black)
      else:
        setColor(myPixel, white)
  writePictureTo(pic, outPath + "\\DrawLine.jpg")

path = "C:\Users\munee_000\Documents\CST 205\Module 3\ImagePortfolio\SourceImages"
outPath = "C:\Users\munee_000\Documents\CST 205\Module 3\ImagePortfolio\GeneratedImages"
pic = makePicture(path + "\\CSUMB Landscape.jpg")
BnWLineImg(pic)
