This is a program to generate A-level year 1 economic diagrams for use in class.

The program is fully object-oriented and was made to be as modular and as good of a framework as possible in order to make it easy to add the many diagrams I wish to complete. Since I chose to work with tkinter as my GUI library which is notoriously bad for modern programming standards I had to implement many modern "fixes" to the libary.

This involved:
A wrapper for the canvas.create_line method so that it could take percentage inputs.
A wrapper for the canvas.create_text method so that it could take percentage inputs.

And most impressively I have managed to create a psuedo CSS flexbox grid system. It works by creating a grid in the page, which is set to sticky="nsew" so that it expands to fill the page. It is then split perfectly evenly into a 15x15 grid by applying even weights to each column and row. Now we have a 15x15 frame that will expand to fill the screen evenly.
When we wish to create a boxed widget, we simply put it in a sub frame that fills the cells we wish the widget to be in, but then we set the sub frame to not propagate so that when we pack the widget it cannot force the sub frame to expand and therefore the 15x15 grid remains unaffected no matter how large a font is or how much padding we give an object.

In the future I may put this flexbox technology into a python library so that it's easier for others to create their own STRICTLY controlled pages easily.

If you wish to add a new diagram, please create a pull request and create a new class that inherits the BasePage class in order to seamlessly integrate it into the project. All help would be appreciated massively.



