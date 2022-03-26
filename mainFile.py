#main gostishevo
import fastWindow
from PIL import Image,ImageTk
testImage = Image.open("./assets/1.png")
testWindow = fastWindow.fastWindow(windowTitle="Ура библиотека работает",image=testImage)
testWindow.kickStart()