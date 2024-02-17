from tkinter import *
# import keyboard

# keyboard = input("введіть @")
# keyboard.add_abbreviation("@", "john@stackabuse.com")

# my_windows = Tk()

# my_windows.title("")
# my_windows.minsize(50,50)
# my_windows.maxsize(60,60)
# my_windows.geometry("600x500+450+150")
# #my_windows.resizable()
# my_windows.mainloop()

# N = int(input("Кількість елементів списку "))
# l = [] # Створюємо порожній список
# for i in range(N):
#  x = input("Задайте %d-й елемент списку " % (i))
#  l.append(x) # Додаємо елемент х у список
# # ==================================
# # Виведення списку на екран
# print(l) 

# This program displays an empty window.
# import tkinter
# class MyGUI:
#  def __init__(self):
#     self.main_window = tkinter.Tk()
#     self.top_frame = tkinter.Frame(self.main_window)
#     self.bottom_frame = tkinter.Frame(self.main_window)
#     self.label1 = tkinter.Label(self.top_frame,
#     text='Winken')
#     self.label2 = tkinter.Label(self.top_frame,
#     text='Blinken')
#     self.label3 = tkinter.Label(self.top_frame,
#     text='Nod')
#     self.label1.pack(side='top')
#     self.label2.pack(side='top')
#     self.label3.pack(side='top')
#     self.label4 = tkinter.Label(self.bottom_frame,
#     text='Winken')
#     self.label5 = tkinter.Label(self.bottom_frame,
#     text='Blinken')
#     self.label6 = tkinter.Label(self.bottom_frame,
#     text='Nod')
#     self.label4.pack(side='left')
 
#     self.label5.pack(side='left')
#     self.label6.pack(side='left')
#     self.top_frame.pack()
#     self.bottom_frame.pack()
#     tkinter.mainloop()
# if __name__ == '__main__':
#  my_gui = MyGUI()
# from tkinter import *

# root = Tk()
# root.title('Product List')

# # Frames
# frameButtons = Frame(root)
# frameListBoxProducts = LabelFrame(root, text='Список покупок')
# frameListBoxBought = LabelFrame(root, text='Купленные товары')
# frameAdditionalButtons = Frame(root)

# frameListBoxProducts.pack(side=LEFT, expand=1, fill=BOTH, padx=5,pady=5)
# frameButtons.pack(side=LEFT)
# frameAdditionalButtons.pack(side=RIGHT, padx=5)
# frameListBoxBought.pack(side=RIGHT, expand=1, fill=BOTH,padx=5,pady=5)

# products = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple', 'milk', 'tomato']

# def btnProductsBought_Event(_listBoxGet, _listBoxInsert):
#     select = list(_listBoxGet.curselection())
#     select.reverse()
#     for i in select:
#         _listBoxInsert.insert(END,_listBoxGet.get(i))
#         _listBoxGet.delete(i)

# def btnAdd_Event():
#     try:
#         if entryProductName.get()!= '':
#             listBoxProducts.insert(END,entryProductName.get())
#             entryProductName.delete(0,END)
#     except:
#         None

# def btnDelete_Event():
#     select = list(listBoxProducts.curselection())
#     select.reverse()
#     for i in select:
#         listBoxProducts.delete(i)

# # ListBoxes
# listBoxProducts = Listbox(frameListBoxProducts, selectmode=EXTENDED)
# listBoxProducts.pack(side=LEFT, expand=1, fill=BOTH)
# scrollListBoxProducts = Scrollbar(frameListBoxProducts, command = listBoxProducts.yview)
# scrollListBoxProducts.pack(side=RIGHT, fill=Y)
# listBoxProducts.config(yscrollcommand=scrollListBoxProducts.set)

# listBoxBoughtProducts = Listbox(frameListBoxBought, selectmode=EXTENDED)
# listBoxBoughtProducts.pack(side=LEFT, expand=1, fill=BOTH)
# scrollListBoxBought = Scrollbar(frameListBoxBought, command = listBoxBoughtProducts.yview)
# scrollListBoxBought.pack(side=RIGHT, fill=Y, anchor=E)
# listBoxBoughtProducts.config(yscrollcommand=scrollListBoxBought.set)

# # Buttons Frame
# btnBougth = Button(frameButtons, text='>>>', width=3, height=1, command=lambda: btnProductsBought_Event(listBoxProducts,listBoxBoughtProducts))
# btnBougth.pack()
# btnProducts = Button(frameButtons, text='<<<', width=3, height=1, command=lambda: btnProductsBought_Event(listBoxBoughtProducts,listBoxProducts))
# btnProducts.pack()

# # Additional Frame
# entryProductName = Entry(frameAdditionalButtons, width=23)
# entryProductName.pack()
# btnAdd = Button(frameAdditionalButtons, text='Добавить новый товар', command=btnAdd_Event)
# btnAdd.pack()
# btnDelete = Button(frameAdditionalButtons, text='Удалить товар', command=btnDelete_Event)
# btnDelete.pack()


# for i in products:
#     listBoxProducts.insert(END,i)

# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title('Events')
# menuFrame = Frame(root)

# def changeTextBoxSize(event):
#     try:
#         if entryHeight.get() != '' and entryWidth.get() != '':
#             textBox.config(height=entryHeight.get(), width=entryWidth.get())
#     except Exception as e:
#         print(e)

# def changeTextBoxBg(event, color):
#     textBox.config(bg=color)

# entryWidth = Entry(menuFrame, width=3)
# entryHeight = Entry(menuFrame, width=3)
# button = Button(menuFrame,text='Изменить')
# textBox = Text(bg='lightgrey')

# menuFrame.pack()
# button.pack(side=RIGHT, padx=5)
# entryWidth.pack(side=BOTTOM)
# entryHeight.pack(side=BOTTOM)
# textBox.pack(fill=BOTH, pady=5)

# button.bind('<Button-1>', changeTextBoxSize) #ЛКМ
# entryWidth.bind('<Return>', changeTextBoxSize) #Enter
# entryHeight.bind('<Return>', changeTextBoxSize) #Enter

# textBox.bind('<FocusIn>', lambda event, color='white': changeTextBoxBg(event, color))
# textBox.bind('<FocusOut>', lambda event, color='lightgrey': changeTextBoxBg(event, color))

# root.mainloop()

