import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.configure(bg="#f2f2f2")
        self.current_player = "X"
        self.board = [""] * 9

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Tic Tac Toe", font=("Helvetica Neue", 24, "bold"),
                         bg="#f2f2f2", fg="#333")
        title.pack(pady=20)

        self.buttons = []
        grid_frame = tk.Frame(self.root, bg="#f2f2f2")
        grid_frame.pack()

        for i in range(9):
            btn = tk.Button(grid_frame, text="", font=("Helvetica Neue", 32),
                            width=4, height=2, bg="#FFFFFF", fg="#000000",
                            command=lambda i=i: self.handle_click(i))
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        self.status_label = tk.Label(self.root, text="Player X's turn", font=("Helvetica Neue", 16),
                                     bg="#f2f2f2", fg="#444")
        self.status_label.pack(pady=10)

        reset_btn = tk.Button(self.root, text="Restart Game", font=("Helvetica Neue", 14),
                              bg="#4CAF50", fg="#fff", command=self.reset_game)
        reset_btn.pack(pady=10)

    def handle_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
            elif "" not in self.board:
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        wins = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
        return any(all(self.board[i] == player for i in combo) for combo in wins)

    def show_winner(self, player):
        self.status_label.config(text=f"Player {player} wins!")
        messagebox.showinfo("Game Over", f"🎉 Player {player} wins!")
        self.disable_buttons()

    def show_draw(self):
        self.status_label.config(text="It's a draw!")
        messagebox.showinfo("Game Over", "It's a draw!")
        self.disable_buttons()

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text="", state=tk.NORMAL)
        self.status_label.config(text="Player X's turn")

# --- Run the app ---
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
