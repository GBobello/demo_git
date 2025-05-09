from tkinter import Tk
from src.calculator import CalculatorApp

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600")
    app = CalculatorApp(root)
    root.mainloop()
    # calculator = CalculatorApp(root)
    # root.mainloop()
