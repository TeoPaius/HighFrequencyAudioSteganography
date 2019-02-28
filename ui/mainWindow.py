import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

import numpy as np

#
# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")
#
# fig = Figure(figsize=(5, 4), dpi=100)
# t = np.arange(0, 3, .01)
# fig.add_subplot(211).plot(t, 2 * np.sin(2 * np.pi * t))
# fig.add_subplot(212).plot(t, 2 * np.sin(2 * np.pi * t))
#
# canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
# canvas.draw()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#
# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#
#
# def on_key_press(event):
#     print("you pressed {}".format(event.key))
#     key_press_handler(event, canvas, toolbar)
#
#
# canvas.mpl_connect("key_press_event", on_key_press)
#
#
# def _quit():
#     root.quit()     # stops mainloop
#     root.destroy()  # this is necessary on Windows to prevent
#                     # Fatal Python Error: PyEval_RestoreThread: NULL tstate
#
#
# button = tkinter.Button(master=root, text="Quit", command=_quit)
# button.pack(side=tkinter.BOTTOM)
#
# tkinter.mainloop()
from fileIO.fileIO import read_whole
from myMath.fourier import timeToFrequency
from testing.config import inputFilePath, scanWindow


class MainWindow(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()
        self.bindEvents()

    def initUI(self):
        self.master.title("Buttons")
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.inputFrame = Frame(self, background="red", borderwidth=3,height=50)
        self.mainFrame = Frame(self, background="blue", borderwidth=3)

        self.ent = ttk.Entry(self.inputFrame)
        self.ent.insert(0,"Input filename")

        self.load_Button = Button(self.inputFrame, text="Load file", command=self.loadGraph)
        self.load_Button.grid(row=0, rowspan=2, column=1,sticky="nes")

        self.out = ttk.Entry(self.inputFrame)
        self.out.insert(0, "Output filename")

        self.ent.grid(row=0, column = 0)
        self.out.grid(row=1, column=0)
        self.inputFrame.grid(row=0, column=0, sticky="nsew")
        self.mainFrame.grid(row=1, column=0, sticky='nsew')
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.plot1 = self.fig.add_subplot(211)
        self.plot1.plot(t, 2 * np.sin(2 * np.pi * t))
        self.plot2 = self.fig.add_subplot(212)
        self.plot2.plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.mainFrame)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(self.canvas, self.mainFrame)
        toolbar.update()

        self.grid(row=0, column=0,sticky="nswe")
        # self.pack(anchor = "nw", fill="both")

    def bindEvents(self):
        self.out.bind("<FocusIn>", lambda event,: {self.out.delete(0, "end")})
        self.out.bind("<FocusOut>", lambda event,: {self.out.insert(0, "Output filename") if self.out.get() == "" else False})
        self.ent.bind("<FocusIn>", lambda event,: {self.ent.delete(0, "end")})
        self.ent.bind("<FocusOut>", lambda event,: {self.ent.insert(0, "Input filename")if self.ent.get() == "" else False })


    def loadGraph(self):
        print("Loading graph")
        t = np.arange(0, 3, .01)
        self.plot1.clear()
        duration = 3
        inputFilePath = "../input/"+self.ent.get()
        rt, params = read_whole(inputFilePath, duration)
        frames = rt
        startOffset = 1
        duration = 0.5

        frq, db, fg = timeToFrequency([i[0] for i in frames[int(startOffset * params.framerate):int(
            (startOffset + duration) * params.framerate) + 1]], params.framerate, duration, startOffset)
        self.fig.clf()

        self.fig.add_subplot(211).plot(fg[0], fg[1])
        self.fig.add_subplot(212).plot(fg[2], fg[3])
        self.canvas.draw()

    def __del__(self):
        plt.close()



def main():
    root = Tk()
    root.geometry("1000x800+100+300")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app = MainWindow(root)
    root.mainloop()



if __name__ == '__main__':
    main()