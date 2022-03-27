#module fastWindow
from tkinter import Tk,Canvas
import ctypes
import markers
from PIL import ImageTk,Image

class fastWindow:
	def __init__(self,windowTitle="Default Title",imagePath=None):
		self.windowTitle = windowTitle
		self.imagePath = imagePath
		self.window = None
		self.markers = []
		self.canvas = None
		self.created = False
		self.image = None
		self.imageData = None
		user32 = ctypes.windll.user32
		self.screenX = user32.GetSystemMetrics(0)
		self.screenY = user32.GetSystemMetrics(1)
		self.binded = False
		self.motionBind = None
		self.clickBind = None

	def getCenter(self,windowsize):
		windowX,windowY = windowsize
		size = f"{windowX}x{windowY}+{abs(int((self.screenX/2) - (windowX/2)))}+{abs(int((self.screenY/2) - (windowY/2)))}"
		print(size)
		return size

	def readImage(self):
		if(self.imagePath != None):
			print("Reading image...")
			self.image = Image.open(self.imagePath)
			self.resize_image()

	def resize_image(self):
		if(self.image.height > self.screenY):
			self.image = self.image.resize((self.image.width,self.screenY))
		if(self.image.width > self.screenX):
			self.image = self.image.resize((self.screenX,self.image.height))

	def create_window(self):
		self.created = True
		self.readImage()
		self.window = Tk()
		self.window.wm_attributes("-transparent","purple")
		self.window.title(self.windowTitle)
		if(self.image != None):
			self.imageData = ImageTk.PhotoImage(self.image)
			self.window.geometry(self.getCenter((self.imageData.width(),self.imageData.height())))
			self.canvas = Canvas(width=self.imageData.width(),height=self.imageData.height())
			self.canvas.pack()
			self.canvas.create_image(0,0,image=self.imageData,anchor="nw")

	def start_window(self):
		self.window.mainloop()

	def passCallback():
		pass

	def destroySelf(self):
		if(self.window != None):
			if(self.binded):
				self.canvas.unbind("<Motion>",self.motionBind)
				self.canvas.unbind("<Button-1>",self.clickBind)
			self.created = False
			self.window.destroy()

	def updMoveMarkers(self,event):
		for mark in self.markers:
			mark.handle(event=event)

	def clickMarkers(self,event):
		for mark in self.markers:
			mark.handleClick(event)

	def add_marker(self,x=0,y=0,r=5,color="white",text="Default Text",callback=None):
		if self.created:
			if(callback == None):
				self.markers.append(markers.marker(posX=x,posY=y,diameter=r,color=color,textDesc=text,callback=self.passCallback,canvas=self.canvas,window=self.window))
			else:
				self.markers.append(markers.marker(posX=x,posY=y,diameter=r,color=color,textDesc=text,callback=callback,canvas=self.canvas,window=self.window))
			if(self.binded == False):
				self.bindMotions()
		else:
			print("Window is not created! Create window then try again")

	def bindMotions(self):
		self.binded = True
		self.motionBind = self.canvas.bind("<Motion>",self.updMoveMarkers)
		self.clickBind = self.canvas.bind("<Button-1>",self.clickMarkers)




