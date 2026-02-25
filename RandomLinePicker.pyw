import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import random


class RandomLinePicker:
    def __init__(self):

        self._window = tk.Tk()
        self._window.geometry("1280x720")
        self._window.state("zoomed")
        self._window.title("Random Line Picker")
        self._window.grid_rowconfigure(0, weight=1)
        self._window.grid_columnconfigure(0, weight=1)

        self._textFont = tkFont.Font(name="Helvetica", weight=tkFont.BOLD)
        self._window.bind("<Configure>", self._onWindowResize)

        self._randomWord = tk.Label(self._window, font=self._textFont)
        self._randomWord.grid(row=0, column=0, sticky=tk.NSEW)
        self._randomWord.pack(fill=tk.BOTH, expand=True)

        self._window.bind("<space>", self._nextLine)
        self._window.bind("t", self._askAndLoadFile)
        self._window.bind("<Escape>", self._exit)

        self._askAndLoadFile()
        self._window.mainloop()


    def _onWindowResize(self, event):
        self._textFont.config(size=-int(event.width / 1920 * 100))


    def _nextLine(self, *_):
        line = ""
        if self._lineList:
            line = self._lineList.pop()
            
        self._randomWord.config(text=line)


    def _exit(self, *_):
        self._window.destroy()


    def _askAndLoadFile(self, *_):
        self._window.update()
        filePath = filedialog.askopenfilename(initialdir=".", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))

        self._lineList = []
        with open(filePath, "r", encoding='utf-8') as file:
            for line in file:
                if line.strip() != "":
                    self._lineList.append(line.strip())
        
        random.shuffle(self._lineList)
        self._nextLine()


if __name__ == "__main__":
    RLP = RandomLinePicker()