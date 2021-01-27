from tkinter import *

class calculator:
	'''
	This is a calculator class and we can make objects from this.
	It has attributes and methods
	'''


	def  __init__(self,title_name = 'calculator',theme = 'white'):
		'''
		This is constructor for the calculator class.It has attributes
		'''
		self.title = title_name
		self.theme = theme
		self.num_list = []
		self.string = ''
		self.a = 0
		self.my_operator = ''
		self.root1 = Tk()
		self.temp = 0

	def initialize_root_title(self):
		'''
		This method creates a root windows using Tkinter module.
		assigns title to the root window and initializes menu
		'''
		self.root1.title(self.title)
		my_menu = Menu(self.root1)
		self.root1.config(menu = my_menu)

		File_menu = Menu(my_menu)
		my_menu.add_cascade(label = 'File',menu= File_menu)
		File_menu.add_command(label = 'exit' , command = self.root1.quit)


		color_menu = Menu(my_menu)
		my_menu.add_cascade(label = 'color change',menu= color_menu)
		color_menu.add_command(label = 'red' , command = lambda: self.change_color('red'))
		color_menu.add_command(label = 'orange' , command = lambda: self.change_color('orange'))
		color_menu.add_command(label = 'yellow' , command = lambda: self.change_color('yellow'))
		color_menu.add_command(label = 'green' , command = lambda: self.change_color('green'))
		color_menu.add_command(label = 'blue' , command = lambda: self.change_color('blue'))
		color_menu.add_command(label = 'pink' , command = lambda: self.change_color('pink'))

	def initialize_buttons(self):
		'''
		This method creates and places buttons into root windows.
		'''
		self.screen = Entry(self.root1,width = 35 , bd = 5)
		self.screen.grid(row = 0 , column = 0 , columnspan = 3 , sticky = E + W)

		button1 = Button(self.root1, text = '1',padx=40,pady=20 ,command = lambda:self.show_my_num(1) , bg = self.theme)
		button2 = Button(self.root1, text = '2',padx=40,pady=20,command = lambda:self.show_my_num(2), bg = self.theme)
		button3 = Button(self.root1, text = '3',padx=40,pady=20,command =lambda: self.show_my_num(3), bg = self.theme)

		button4 = Button(self.root1, text = '4',padx=40,pady=20,command =lambda: self.show_my_num(4), bg = self.theme)
		button5 = Button(self.root1, text = '5',padx=40,pady=20,command =lambda: self.show_my_num(5), bg = self.theme)
		button6 = Button(self.root1, text = '6',padx=40,pady=20,command =lambda: self.show_my_num(6), bg = self.theme)

		button7 = Button(self.root1, text = '7',padx=40,pady=20,command =lambda: self.show_my_num(7), bg = self.theme)
		button8 = Button(self.root1, text = '8',padx=40,pady=20,command =lambda: self.show_my_num(8), bg = self.theme)
		button9 = Button(self.root1, text = '9',padx=40,pady=20,command =lambda: self.show_my_num(9), bg = self.theme)

		button_zero = Button(self.root1, text = '0',padx=40,pady=20,command =lambda: self.show_my_num(0), bg = self.theme)
		button_plus = Button(self.root1, text = '+',padx=40,pady=20,command = lambda: self.operator('+'), bg = self.theme)
		button_equal = Button(self.root1, text = '=',pady=20,command = self.equal_operator, bg = self.theme)

		button_sub = Button(self.root1, text = '-',padx=40,pady=20,command = lambda: self.operator('-'), bg = self.theme)
		button_mul = Button(self.root1, text = '*',padx=40,pady=20,command = lambda: self.operator('*'), bg = self.theme)
		button_clear = Button(self.root1, text = 'clear',padx=30,pady=20,command = self.clear, bg = self.theme)
		button_div = Button(self.root1, text = '/',padx=40,pady=20,command = lambda: self.operator('/'), bg = self.theme)

		button1.grid(row=1,column=0,padx=5,pady=5)
		button2.grid(row=1,column=1,padx=5,pady=5)
		button3.grid(row=1,column=2,padx=5,pady=5)

		button4.grid(row=2,column=0,padx=5,pady=5)
		button5.grid(row=2,column=1,padx=5,pady=5)
		button6.grid(row=2,column=2,padx=5,pady=5)

		button7.grid(row=3,column=0,padx=5,pady=5)
		button8.grid(row=3,column=1,padx=5,pady=5)
		button9.grid(row=3,column=2,padx=5,pady=5)

		button_zero.grid(row=4,column=0,padx=5 ,pady=5)
		button_plus.grid(row=4,column=2,rowspan =2,padx=5,pady=5,sticky = N+S)
		button_clear.grid(row=4,column=1,padx=5,pady=5)
		
		button_sub.grid(row=5,column=0,padx=5,pady=5)
		button_mul.grid(row=5,column=1,padx=5,pady=5)
		button_div.grid(row=6,column=0,padx=5,pady=5)
		button_equal.grid(row=6,column=1,columnspan=2,padx=5,pady=5,sticky = W+E)
		

	def equal_operator(self,state = True):
		'''
		This method produces the final output in the calculator
		'''
		try :
			if state:
				self.clear()
				b = int(self.string)
				if self.my_operator == '+':
					self.screen.insert(0,str(self.a)+''+str(self.my_operator)+''+str(b)+''+'='+str(self.a+b))
				elif self.my_operator == '-':
					self.screen.insert(0,str(self.a)+''+str(self.my_operator)+''+str(b)+''+'='+str(self.a-b))
				elif self.my_operator == '*':
					self.screen.insert(0,str(self.a)+''+str(self.my_operator)+''+str(b)+''+'='+str(self.a*b))
				elif self.my_operator == '/':
					self.screen.insert(0,str(self.a)+''+str(self.my_operator)+''+str(b)+''+'='+str(self.a/b))
			elif state == False:
				self.clear()
				b = int(self.string)
				if self.my_operator == '+':
					self.temp = self.a+b
					self.screen.insert(0,str(self.temp))
				elif self.my_operator == '-':
					self.temp = self.a-b
					self.screen.insert(0,str(self.temp))
				elif self.my_operator == '*':
					self.temp = self.a*b
					self.screen.insert(0,str(self.temp))
				elif self.my_operator == '/':
					self.temp = self.a/b
					self.screen.insert(0,str(self.temp))
				
			
		except ValueError:
			print('Enter your numbers,operator first')

		self.num_list = []
		self.string = ''
		self.a = 0
		self.my_operator = ''


	def show_my_num(self,x):
		self.num_list.append(x)
		self.string = ''
		for i in self.num_list:
			self.string = self.string + str(i)
		current=self.screen.get()
		self.screen.delete(0,END)
		to_show=str(current)+str(x)
		self.screen.insert(0,to_show)

	def clear(self):
		'''
		This method clears the entry screen and all the stored value
		'''
		self.screen.delete(0,END)
		self.num_list.clear()

	def operator(self,x):
		'''
		This method clears the screen and stores the operator character pressed by the user
		'''
		try :
			if self.my_operator != '' and self.string != '':
				self.equal_operator(state = False)
				self.string = str(self.temp)
				self.clear()
				self.operator(x)

			else :
				self.clear()
				self.a = int(self.string)
				self.my_operator = x
				self.screen.insert(0,str(self.a)+''+x)
			
		except ValueError:
			print('Enter your number first')
		

	def start_calc(self):
		'''
		This starts the calculator
		'''
		self.initialize_root_title()
		self.initialize_buttons()
		self.root1.mainloop()

	


	def change_color(self,x):
		'''
		This method or function changes the color of calculator
		'''
		self.theme = x
		self.end_calc()
		self.start_calc()

	def __str__(self):
		return self.title




SoniyaKc_calc = calculator('Soniya','pink')
SoniyaKc_calc.start_calc()


