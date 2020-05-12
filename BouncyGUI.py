from tkinter import *
import math

class BouncyGUI(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Bouncy")
        self.grid()

        # Label and field for the height
        self._heightLabel = Label(self, text = "Initial Height: ")
        self._heightLabel.grid(row = 0, column = 0)
        self._heightVar = DoubleVar()
        self._heightEntry = Entry(self,
                                  textvariable = self._heightVar)
        self._heightEntry.grid(row = 0, column = 1)

        # Label and field for the index
        self._indexLabel = Label(self, text = "Index: ")
        self._indexLabel.grid(row = 1, column = 0)
        self._indexVar = DoubleVar()
        self._indexEntry = Entry(self,
                                textvariable = self._indexVar)
        self._indexEntry.grid(row = 1, column = 1)

        # Label and field for the bounces
        self._bouncesLabel = Label(self, text = "Number of bounces: ")
        self._bouncesLabel.grid(row = 2, column = 0)
        self._bouncesVar = IntVar()
        self._bouncesEntry = Entry(self,
                                textvariable = self._bouncesVar)
        self._bouncesEntry.grid(row = 2, column = 1)

        # The command buton
        self._button = Button(self,
                              text = "Compute",
                              command = self._compute)
        self._button.grid(row = 3, column = 0, columnspan = 2)

        # Label and field for the index
        self._distanceLabel = Label(self, text = "Total distance: ")
        self._distanceLabel.grid(row = 4, column = 0)
        self._distanceVar = DoubleVar()
        self._distanceEntry = Entry(self,
                                textvariable = self._distanceVar)
        self._distanceEntry.grid(row = 4, column = 1)

    def _compute(self):
        """Event handler for the button."""
        height = self._heightVar.get()
        index = self._indexVar.get()
        bounces = self._bouncesVar.get()
        total = 0
        for x in range(bounces):
            total += height
            height *= index
            total += height
        self._distanceVar.set(total)


def main():
    """Instantiate and pop up the window."""
    BouncyGUI().mainloop()

main()
