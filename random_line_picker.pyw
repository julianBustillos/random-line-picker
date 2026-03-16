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

        self._textfont = tkFont.Font(name="Helvetica", weight=tkFont.BOLD)
        self._window.bind("<Configure>", self._on_window_resize)

        self._random_word = tk.Label(self._window, font=self._textfont)
        self._random_word.grid(row=0, column=0, sticky=tk.NSEW)
        self._random_word.pack(fill=tk.BOTH, expand=True)

        self._window.bind("l", self._askloadfile)
        self._window.bind("r", self._loadfile)
        self._window.bind("<space>", self._nextline)
        self._window.bind("<Right>", self._nextline)
        self._window.bind("<Left>", self._prevline)
        self._window.bind("f", self._tooglefullscreen)
        self._window.bind("<Escape>", self._exit)

        self._askloadfile()
        self._window.mainloop()

    def _on_window_resize(self, event):
        self._textfont.config(size=-int(event.width / 1920 * 100))

    def _askloadfile(self, *_):
        self._window.update()
        self._filepath = filedialog.askopenfilename(
            initialdir=".",
            title="Select a File",
            filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
        )
        self._loadfile()

    def _loadfile(self, *_):
        try:
            linelist = []
            with open(self._filepath, "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip() != "":
                        linelist.append(line.strip())
        except Exception:
            return

        self._linelist = linelist
        random.shuffle(self._linelist)
        self._currline_id = -1
        self._nextline()

    def _nextline(self, *_):
        if self._currline_id < len(self._linelist):
            self._currline_id += 1
        self._showline()

    def _prevline(self, *_):
        if self._currline_id > 0:
            self._currline_id -= 1
        self._showline()

    def _showline(self):
        self._random_word.config(
            text=(
                self._linelist[self._currline_id]
                if self._currline_id < len(self._linelist)
                else ""
            )
        )

    def _tooglefullscreen(self, *_):
        value = self._window.attributes("-fullscreen")
        self._window.attributes("-fullscreen", not value)

    def _exit(self, *_):
        self._window.destroy()


if __name__ == "__main__":
    rlp = RandomLinePicker()
