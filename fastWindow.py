#module fastWindow
from tkinter import Tk,Canvas
import ctypes
import markers
from PIL import ImageTk

class fastWindow:
	def __init__(self,windowTitle="Default Title",image=None):
		self.windowTitle = windowTitle
		self.image = image
		self.window = None
		self.markers = []
		self.canvas = None
		self.created = False
		self.imageData = None
		user32 = ctypes.windll.user32
		self.screenX = user32.GetSystemMetrics(0)
		self.screenY = user32.GetSystemMetrics(1)

	def getCenter(self,windowsize):
		windowX,windowY = windowsize
		size = f"{windowX}x{windowY}+{abs(int((self.screenX/2) - (windowX/2)))}+{abs(int((self.screenY/2) - (windowY/2)))}"
		print(size)
		return size

	def resize_image(self):
		if(self.image.height > self.screenY):
			self.image = self.image.resize((self.image.width,self.screenY))
		if(self.image.width > self.screenX):
			self.image = self.image.resize((self.screenX,self.image.height))

	def create_window(self):
		self.window = Tk()
		self.window.title(self.windowTitle)
		if(self.image != None):
			self.resize_image()
			self.imageData = ImageTk.PhotoImage(self.image)
			self.window.geometry(self.getCenter((self.imageData.width(),self.imageData.height())))
			self.canvas = Canvas(master=self.window)
			self.canvas.pack()
			self.canvas.create_image(0,0,image=self.imageData,anchor="nw")

	def start_window(self):
		self.window.mainloop()

	def kickStart(self):
		self.create_window()
		self.start_window()

	def passCallback():
		pass

	def add_marker(self,x=0,y=0,r=5,color="white",text="Default Text",callback=None):
		if self.created:
			if(callback == None):
				self.markers.append(markers.marker(posX=x,posY=y,diameter=r,color=color,textDesc=text,callback=self.passCallback,canvas=self.canvas,window=self.window))
			else:
				self.markers.append(markers.marker(posX=x,posY=y,diameter=r,color=color,textDesc=text,callback=callback,canvas=self.canvas,window=self.window))
		else:
			print("Window is not created! Create window then try again")




