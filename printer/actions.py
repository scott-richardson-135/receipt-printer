from .connection import getPrinter

def print_custom_message(message):
    printer = getPrinter()
    printer.text(message)
    printer.cut()
    printer.close()
