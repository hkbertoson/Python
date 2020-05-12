from tkinter import *


class Temp(Frame):
    def __init__(self):
        Frame.__init__(self)
        ##        self._fahren = 0.0
        ##        self._cel = 0.0
        self.master.title("TempConver")
        self.grid()
        self._fahrenLabel = Label(self, text="Fahrenheit")
        self._fahrenLabel.grid(row=0, column=0)
        self._fahrenVar = DoubleVar()
        self._fahrenEntry = Entry(self, textvariable=self._fahrenVar)
        self._fahrenEntry.grid(row=1, column=0)
         self._celLabel = Label(self, text="Celcius")
        self._celLabel.grid(row=0, column=2)
        self._celVar = DoubleVar()
        self._celEntry = Entry(self, textvariable=self._celVar)
        self._celEntry.grid(row=1, column=2)
        self._fahrenButton = Button(self, text=">>>>", command=self.FtoC)
        self._fahrenButton.grid(row=0, column=1)
        self._celButton = Button(self, text="<<<<", command=self.CtoF)
        self._celButton.grid(row=1, column=1)

    def FtoC(self):
        fahren = self._fahrenVar.get()
        cel = (5 / 9) * (fahren - 32)
        self._celVar.set(cel)

    def CtoF(self):
        cel = self._celVar.get()
        fahren = (9 / 5) * (cel + 32)
        self._fahrenVar.set(fahren)


def main():
    Temp().mainloop()


main()
