######## HOMEWORKS ##########

def rettangoloBello(pic):
    coloreBello=pickAColor()
    for x in range(getWidth(pic)/8,getWidth(pic)/2):
      for y in range(getHeight(pic)/4,getHeight(pic)/3):
         pix=getPixel(pic,x,y)
         setColor(pix,coloreBello)
         
def pratoFiorito():
  fiore1= makePicture("C:\Users\Andrea\Desktop\Universitaaa\Fondamenti di Informatica\immagini campione\mediasources\mediasources-4ed\flower1.jpg")
  fiore2= makePicture("C:\Users\Andrea\Desktop\Universitaaa\Fondamenti di Informatica\immagini campione\mediasources\mediasources-4ed\flower2.jpg")
  canvas= makeEmptyPicture(700,150)
  copia_da_coordinata(fiore1,canvas,0,10)
  copia_da_coordinata(fiore2,canvas,100,10)
  copia_da_coordinata(nega(fiore1),canvas,200,10)
  copia_da_coordinata(togliBlu(fiore2),canvas,300,10)
  copia_da_coordinata(togliRosso(nega(fiore1)), canvas, 400, 10)
  
def nega(pic):
#@param pic: Picture
  for x in getPixels(pic):
    rosso=getRed(x)
    verde=getGreen(x)
    blu=getBlue(x)
    colorNegativo=makeColor(255-rosso,255-verde,255-blu)
    setColor(x,colorNegativo)
    
def togliRosso(pic):
# @param pic: Picture
 for x in getPixels(pic):
   setRed(x,0)
   
def togliBlu(pic):
#@param pic:Picture
  for x in getPixels(pic):
     setBlue(x,0)

def copia_da_coordinata(pic,canvas,ascissa,ordinata):
# @parama pic: picture
# @param canvas : Picture (canvas)
# @param ascisssa : integer     ascissa del punto da cui inizio a copiare
# @param ordinata : integer     ordinata del punto da cui inizio a copiare
  for sourceX in range(0,getWidth(pic)):
    targetX=sourceX+ascissa
    for sourceY in range(0, getHeight(pic)):
      targetY=sourceY+ordinata
      color=getColor(getPixel(pic,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
    
