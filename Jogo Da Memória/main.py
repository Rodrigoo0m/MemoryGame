import random
import tkinter as tk

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Memória")
        
        self.cards = ['🍎', '🍌', '🍓', '🍇', '🍒', '🍉', '🍍', '🍊', '🍏', '🍐', '🥭', '🍋']
        self.cards *= 2  # Duplicate cards for pairs
        random.shuffle(self.cards)

        self.buttons = {}
        self.first_selection = None
        self.second_selection = None
        self.pairs_found = 0

        self.create_board()

    def create_board(self):
        for i in range(6):
            for j in range(4):
                button = tk.Button(self.root, text='?', width=10, height=5, command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[(i, j)] = button

    def on_button_click(self, row, col):
        if self.first_selection is None:
            self.first_selection = (row, col)
            self.buttons[(row, col)].config(text=self.cards[row * 4 + col])
        elif self.second_selection is None and (row, col) != self.first_selection:
            self.second_selection = (row, col)
            self.buttons[(row, col)].config(text=self.cards[row * 4 + col])
            self.root.after(1000, self.check_match)

    def check_match(self):
        if self.cards[self.first_selection[0] * 4 + self.first_selection[1]] == self.cards[self.second_selection[0] * 4 + self.second_selection[1]]:
            self.buttons[self.first_selection].config(state='disabled')
            self.buttons[self.second_selection].config(state='disabled')
            self.pairs_found += 1
            if self.pairs_found == len(self.cards) // 2:
                tk.messagebox.showinfo("Parabéns!", "Você encontrou todos os pares!")
        else:
            self.buttons[self.first_selection].config(text='?')
            self.buttons[self.second_selection].config(text='?')

        self.first_selection = None
        self.second_selection = None

root = tk.Tk()
game = MemoryGame(root)
root.mainloop()
