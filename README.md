# Paint App

A simple desktop paint application built with Python and Tkinter. The application provides basic drawing tools, colour selection, brush size control, text support, and the ability to save drawings.

## Features

- Pencil tool for freehand drawing
- Eraser tool
- Line tool
- Rectangle tool
- Oval tool
- Arc tool
- Text tool
- Colour picker
- Adjustable brush size from 1 to 50
- Live shape preview while drawing
- Clear canvas option
- Save drawings as PostScript files
- File menu with Save, Clear, and Exit options
- Simple and responsive desktop interface
- Input dialogs for adding text

## Drawing Tools

### Pencil

Draw freehand lines on the canvas using the selected colour and brush size.

### Eraser

Erase parts of the drawing by drawing over them with the background colour.

### Line

Create straight lines by clicking and dragging across the canvas.

### Rectangle

Draw rectangular shapes with adjustable outline colour and width.

### Oval

Draw oval shapes with adjustable outline colour and width.

### Arc

Create arc shapes using a fixed 150-degree arc.

### Text

Add custom text to the canvas. The text colour follows the currently selected colour.

## Colour Selection

The Colour button opens the Tkinter colour picker.

The selected colour is used by the Pencil, Line, Rectangle, Oval, Arc, and Text tools.

## Brush Size

The brush size can be changed using the size control in the toolbar.

Supported sizes:

    1 - 50

The selected size affects:

- Pencil
- Eraser
- Lines
- Rectangle outlines
- Oval outlines
- Arc outlines

## Save Drawing

The application includes a Save option that allows the current canvas to be saved as a PostScript (`.ps`) file.

To save a drawing:

1. Create your drawing.
2. Click the `Save` button.
3. Choose the file location and filename.
4. Confirm the save operation.

The application displays a confirmation message after a successful save.

## Requirements

- Python 3.8 or newer
- Tkinter

Tkinter is included with most standard Python installations.

## Installation

Clone the repository:

    git clone https://github.com/RaavanHrishi07/Paint-App.git

Move into the project directory:

    cd Paint-App

No external Python packages are required.

## Usage

Run the application:

    python main.py

The Paint App window will open with the drawing canvas and toolbar.

Select a drawing tool and use the mouse to create your drawing.

## Controls

| Control | Function |
| --- | --- |
| Pencil | Freehand drawing |
| Eraser | Erase parts of the drawing |
| Line | Draw straight lines |
| Rectangle | Draw rectangles |
| Oval | Draw ovals |
| Arc | Draw arcs |
| Text | Add text |
| Colour | Select drawing colour |
| Size | Change brush size |
| Save | Save the current drawing |
| Clear | Clear the canvas |
| Exit | Close the application |

## How It Works

1. The application creates a Tkinter window and drawing canvas.
2. Mouse events are captured from the canvas.
3. The selected tool determines how mouse actions are interpreted.
4. Freehand tools draw continuously while the mouse is dragged.
5. Shape tools display a temporary preview while dragging.
6. The final shape is created when the mouse button is released.
7. Text is added through a dialog box.
8. The canvas can be saved as a PostScript file.

## Project Structure

    Paint-App/
    │
    ├── main.py
    ├── .gitignore
    ├── README.md
    └── LICENSE

## Technologies Used

- Python
- Tkinter
- Tkinter Canvas
- Tkinter Color Chooser
- Tkinter File Dialog

## Error Handling

The application handles common user interactions such as:

- Cancelling colour selection
- Cancelling text input
- Cancelling the save dialog
- Invalid brush size values
- Save errors reported by Tkinter

## Author

**Hrishikesh Sharma**

GitHub: https://github.com/RaavanHrishi07

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.