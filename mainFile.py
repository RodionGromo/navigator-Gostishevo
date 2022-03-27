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

	def nextMap():
		mapWindow.destroySelf()
		secondMap()

	def firstMem():
		mapWindow.destroySelf()
		firstMemorial()

	def secondMem():
		mapWindow.destroySelf()
		secondMemorial()

	def thirdMem():
		mapWindow.destroySelf()
		thirdMemorial()

	mapWindow = fastWindow(windowTitle="Карта",imagePath="./assets/map.png")
	mapWindow.create_window()
	mapWindow.add_marker(x=475, y=322, r=15, text="Памятник железнодорожникам",color="gold", callback=thirdMem)
	mapWindow.add_marker(x=879, y=175, r=15, text="Памятник советским воинам-танкистам, павшим у с. Рождественка и с. Непхаево",color="gold",callback=secondMem)
	mapWindow.add_marker(x=1473, y=607, r=15, text="Памятник воинам, погибшим в ВОВ",color="gold",callback=firstMem)
	mapWindow.add_marker(x=275, y=729, r=25, color="red", text="Выйти", callback=exitApp)
	mapWindow.add_marker(x=137, y=528, r=15, text="Следующее место",color="green", callback=nextMap)
	mapWindow.start_window()

def secondMap():

	def prevMap():
		mapWindow.destroySelf()
		createMap()

	def nextMap():
		mapWindow.destroySelf()
		thirdMap()

	def firstMem():
		mapWindow.destroySelf()
		forthMemorial()

	mapWindow = fastWindow(windowTitle="Карта №2",imagePath="./assets/map2.png")
	mapWindow.create_window()
	mapWindow.add_marker(x=506,y=74,r=15, text="Назад",color="red", callback=prevMap)
	mapWindow.add_marker(x=389,y=510,r=15, text="Памятник скорбящей гражданской женщине",color="gold",callback=firstMem)
	mapWindow.add_marker(x=488,y=183,r=15, text="Следующее место",color="green", callback=nextMap)
	mapWindow.start_window()

def thirdMap():
	def firstMem():
		mapWindow.destroySelf()
		fifthMemorial()

	def goBack():
		mapWindow.destroySelf()
		secondMap()

	def nextMap():
		mapWindow.destroySelf()
		forthMap()

	mapWindow = fastWindow(windowTitle="Карта №3",imagePath="./assets/map3.png")
	mapWindow.create_window()
	mapWindow.add_marker(x=380,y=186,r=15,text="Памятник медсанбату №454 и другим воинам 1941-1943 г.г.",color="gold",callback=firstMem)
	mapWindow.add_marker(x=699,y=628,r=15,text="Назад",color="red",callback=goBack)
	mapWindow.add_marker(x=428,y=117,r=15,text="Следующее место",color="green",callback=nextMap)
	mapWindow.start_window()

def forthMap():
	def firstMem():
		mapWindow.destroySelf()
		sixthMemorial()

	def goBack():
		mapWindow.destroySelf()
		thirdMap()

	def nextMap():
		mapWindow.destroySelf()
		fifthMap()

	mapWindow = fastWindow(windowTitle="Карта №4",imagePath='./assets/map4.png')
	mapWindow.create_window()
	mapWindow.add_marker(x=331,y=301,r=15,text="Памятник морякам 281 полка",color='gold',callback=firstMem)
	mapWindow.add_marker(x=863,y=210,r=15,text="Следующее место",color='green',callback=nextMap)
	mapWindow.add_marker(x=493,y=642,r=15,text="Назад",color="red",callback=goBack)
	mapWindow.start_window()

def fifthMap():

	def goBack():
		mapWindow.destroySelf()
		forthMap()

	def nextMap():
		mapWindow.destroySelf()
		sixthMap()

	def firstMem():
		mapWindow.destroySelf()
		seventhMemorial()

	mapWindow = fastWindow(windowTitle="Карта №5",imagePath="./assets/map5.png")
	mapWindow.create_window()
	mapWindow.add_marker(x=305,y=293,r=15,text="Памятник неизвестным лётчикам",color='gold',callback=firstMem)
	mapWindow.add_marker(x=541,y=281,r=15,text="Следующее место",color='green',callback=nextMap)
	mapWindow.add_marker(x=103,y=234,r=15,text="Назад",color='red',callback=goBack)
	mapWindow.start_window()

def sixthMap():

	def goBack():
		mapWindow.destroySelf()
		fifthMap()

	def gotoFirst():
		mapWindow.destroySelf()
		createMap()

	def firstMem():
		mapWindow.destroySelf()
		eighthMemorial()

	mapWindow = fastWindow(windowTitle="Карта №6",imagePath="./assets/map6.png")
	mapWindow.create_window()
	mapWindow.add_marker(x=689,y=364,r=15,text="Памятник односельчанам, погибшим в годы ВОВ",color='gold',callback='firstMem')
	mapWindow.add_marker(x=910,y=287,r=15,text="Вернуться в самое начало",color="green",callback=gotoFirst)
	mapWindow.add_marker(x=317,y=102,r=15,text="Назад",color='red',callback=goBack)
	mapWindow.start_window()

def eighthMemorial():
	def goBack():
		memorialWindow.destroySelf()
		sixthMap()
	memorialWindow = fastWindow(windowTitle="Памятник односельчанам, погибшим в годы ВОВ",imagePath="./assets/8.png")
	memorialWindow.create_window()
	lb1t = "Историческое событие, с которым связан памятник – 644 фамилии земляков выбито на плитах"
	lb1 = Label(master=memorialWindow.window,text=lb1t,justify='left',wraplength=180)
	lb1.place(x=407,y=509)
	memorialWindow.add_marker(x=490,y=732,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

def seventhMemorial():
	def goBack():
		memorialWindow.destroySelf()
		createMap()
	memorialWindow = fastWindow(windowTitle="Памятник неизвестным лётчикам",imagePath="./assets/7.png")
	memorialWindow.create_window()
	lb1t = "Историческое событие, с которым связан памятник – в мае 1942 года советский бомбардировщик бомбил в г. Белгороде вокзал и нефтебазу и был подбит. Летчик тянул 20 км"
	lb1 = Label(master=memorialWindow.window,text=lb1t,justify='left',wraplength=180)
	lb1.place(x=374,y=105)
	memorialWindow.add_marker(x=457,y=653,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

def sixthMemorial():
	def goBack():
		memorialWindow.destroySelf()
		forthMap()
	memorialWindow = fastWindow(windowTitle="Памятник морякам 281 полка",imagePath="./assets/6.png")
	memorialWindow.create_window()
	lb1t = "Историческое событие, с которым связан памятник – ожесточенные бои с 7 по 15 июля 1943 года в районе с. Гостищево за железную дорогу. "
	lb1 = Label(master=memorialWindow.window,text=lb1t,justify='left',wraplength=180)
	lb1.place(x=326,y=129)
	memorialWindow.add_marker(x=360,y=560,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

def fifthMemorial():
	def goBack():
		memorialWindow.destroySelf()
		thirdMap()
	memorialWindow = fastWindow(windowTitle="Памятник медсанбату №454 и другим воинам 1941-1943 г.г.",imagePath="./assets/5.png")
	memorialWindow.create_window()
	lb1t = "Историческое событие, с которым связан памятник – медсестра Галя Буланова спасла жизнь комбату, а сама погибла. А так же в 1943 г. был уничтожен медсанбат №454 с огромным количеством раненых"
	lb1 = Label(master=memorialWindow.window,text=lb1t,justify='left',wraplength=180)
	lb1.place(x=351,y=116)
	memorialWindow.add_marker(x=414,y=563,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

def firstMemorial():
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

def secondMemorial():
	def goBack():
		memorialWindow.destroySelf()
		createMap()

	memorialWindow = fastWindow(windowTitle="Памятник советским воинам-танкистам, павшим у с. Рождественка и с. Непхаево",imagePath="./assets/2.png")
	memorialWindow.create_window()
	lb1 = Label(master=memorialWindow.window,text="Историческое событие, с которым связан памятник – в 1942 году сражение у реки Липовый Донец.",justify="left",wraplength=200)
	lb1.place(x=356,y=70)
	memorialWindow.add_marker(x=500,y=721,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

def thirdMemorial():
	def goBack():
		memorialWindow.destroySelf()
		createMap()
	memorialWindow = fastWindow(windowTitle="Памятник железнодорожникам",imagePath="./assets/3.png")
	memorialWindow.create_window()
	lb1t = "Историческое событие, с которым связан памятник – участие в сражении бронепоезда, восстановление железнодорожного вокзала"
	lb1 = Label(master=memorialWindow.window,text=lb1t,justify='left',wraplength=180)
	lb1.place(x=364,y=313)
	memorialWindow.add_marker(x=481, y=695, r=15, text="Назад", callback=goBack)
	memorialWindow.start_window()

def forthMemorial():
	def goBack():
		memorialWindow.destroySelf()
		secondMap()
	memorialWindow = fastWindow(windowTitle="Памятник скорбящей гражданской женщине, женщине-труженице",imagePath="./assets/4.png")
	memorialWindow.create_window()
	lb1t = "Памятник поставлен в честь женщин, работавших в тылу"
	lb1 = Label(master=memorialWindow.window,text=lb1t,justify='left',wraplength=180)
	lb1.place(x=404,y=67)
	memorialWindow.add_marker(x=509,y=355,r=15,text="Назад",callback=goBack)
	memorialWindow.start_window()

if __name__ == '__main__':
	mainWindow()