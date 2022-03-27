#main gostishevo
from fastWindow import fastWindow
from tkinter import Label,font,Button

def mainWindow():
	def startAdventure():
		mW.destroySelf()
		createMap()
	mW = fastWindow(windowTitle="Навигатор Гостищево")
	mW.create_window()
	lb1 = Label(master=mW.window,text="Добро пожаловать в...")
	lb1.configure(font=font.Font(family="Times New Roman",size=14,weight="bold"))
	lb1.pack()
	lb2 = Label(master=mW.window,text='Навигатор Гостищево')
	lb2.configure(font=font.Font(family="Times New Roman",size=48,weight="normal"))
	lb2.pack()
	btn1 = Button(master=mW.window,text="Начать путешествие!",command=startAdventure)
	btn1.pack()
	mW.start_window()

def createMap():
	def exitApp():		
		mapWindow.destroySelf()

	def firstMem():
		mapWindow.destroySelf()
		firstMemorial()

	def secondMem():
		mapWindow.destroySelf()
		secondMemorial()

	mapWindow = fastWindow(windowTitle="Карта",imagePath="./assets/map.png")
	mapWindow.create_window()
	mapWindow.add_marker(x=475, y=322, r=15, text="Памятник морякам 281 полка", callback=firstMem)
	mapWindow.add_marker(x=879, y=175, r=15, text="Памятник воинам, погибшим в ВОВ",callback=secondMem)
	mapWindow.add_marker(x=275, y=729, r=25, color="red", text="Выйти", callback=exitApp)
	mapWindow.start_window()

def thirdMemorial():
	def goBack():
		memorialWindow.destroySelf()
		createMap()

	memorialWindow = fastWindow(windowTitle="_",imagePath="./assets/_.png")
	memorialWindow.create_window()
	lb1t = "_"
	lb1 = Label(master=memorialWindow.window,text=lb1t,justify='left',wraplength=180)
	lb1.place(x=0,y=0)
	memorialWindow.add_marker(x=0,y=0,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

def secondMemorial():
	def goBack():
		memorialWindow.destroySelf()
		createMap()

	memorialWindow = fastWindow(windowTitle="Памятник воинам, погибшим в ВОВ",imagePath="./assets/1.png")
	memorialWindow.create_window()
	lb1t = "Памятник воинам, погибшим в ВОВ:\n5 декабря 1941 года немцы расстреляли около 50 советских солдат на улице Кирова в с. Гостищево."
	lb1 = Label(master=memorialWindow.window,text=lb1t,justify='left',wraplength=180)
	lb1.place(x=374,y=70)
	memorialWindow.add_marker(x=444,y=704,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

def firstMemorial():
	def goBack():
		memorialWindow.destroySelf()
		createMap()

	memorialWindow = fastWindow(windowTitle="Памятник морякам 281 полка",imagePath="./assets/6.png")
	memorialWindow.create_window()
	lb1 = Label(master=memorialWindow.window,text="Памятник морякам 281 полка:\nОжесточенные бои с 7 по 15 июля 1943 года в районе с. Гостищево за железную дорогу.",justify="left",wraplength=200)
	lb1.place(x=356,y=70)
	memorialWindow.add_marker(x=500,y=721,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

if __name__ == '__main__':
	mainWindow()