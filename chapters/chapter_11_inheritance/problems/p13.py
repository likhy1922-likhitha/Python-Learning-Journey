'''
Parent class: Printer → method print_doc() prints "Printing document"
Child class: ColorPrinter → override print_doc() to print "Printing in color"
Create a ColorPrinter object and call print_doc().
'''
class Printer:
    def docs(self):
        print("Printing documnet")
class ColorPrinter(Printer):
    def docs(self):
        print("Printing in color")
c = ColorPrinter()
c.docs()