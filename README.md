# RandomLinePicker
Python GUI that shows random lines from text file.

## Description
This tkinter python GUI loads a text file containing several lines and display them in a random order. When all line were shown, a blanck line appears.
Some convenient keybindings were added to cover basic needs.
Executable was built using pyinstaller package.

## Getting Started

### Dependencies
* Windows OS

### Installing
* Unzip the latest win release file containing *random_line_picker.exe* along with *example.txt* file.

### Executing program
* Launch *random_line_picker.exe* and choose a txt file to load (e.g. *example.txt*)

### Keybindings
* **L** open explorer to load a new file.
* **R** reload current file (lines are then shuffled in a different order).
* **Space** or **Right arrow** show next line.
* **Left arrow** show previous line.
* **F** toggle full screen mode.
* **Escape** exit the program.

### Text file format
* Each line is loaded to be shown except the empty ones.
* *example.txt* can be used as an example.

## Authors
Julian Bustillos - [bustillosjulian@gmail.com](mailto:bustillosjulian@gmail.com)

## Version History
* 1.0
  * Initial Release

## License
This project is licensed under the GNU GPLv3 License - see the LICENSE.md file for details.