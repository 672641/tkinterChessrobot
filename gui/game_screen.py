import tkinter as tk
from tkinter import messagebox
from components.chessboard import Chessboard  # Import the Chessboard component
from components.move_history import MoveHistory  # Import the MoveHistory component
import chess

def show_game_screen(root, selection_frame, color, difficulty):
    '''Show the game screen with the selected color and difficulty.'''
    
    # Destroy the selection screen
    selection_frame.destroy()

    # Create the main game frame
    game_frame = tk.Frame(root, bg="#1a237e")
    game_frame.pack(fill="both", expand=True)
    
    # Determine whether to flip the board based on the selected color
    flipped = (color == "black")
    
    # Chessboard frame
    board_frame = tk.Frame(game_frame, bg="#1a237e")
    board_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")

    # Define desired square size
    square_size = 100

    # Create the Chessboard component with the specified square size
    board_canvas = Chessboard(board_frame, square_size=square_size, flipped=flipped)
    board_canvas.pack()

    # Update the Chessboard with the starting position
    starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board_canvas.update_board(starting_fen)
    
    # Move history frame
    history_frame = tk.Frame(game_frame, bg="#1a237e")
    history_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")

    # Create the MoveHistory component
    move_history = MoveHistory(history_frame, board_canvas)
    move_history.grid(row=0, column=0, padx=20, pady=20, sticky="n")

    # Action buttons frame
    action_frame = tk.Frame(game_frame, bg="#1a237e")
    action_frame.grid(row=1, column=1, padx=20, pady=20, sticky="e")

    # Confirm Move Button
    confirm_move_button = tk.Button(
        action_frame,
        text="CONFIRM MOVE",
        font=("Helvetica", 20, "bold"),
        bg="#28a745",  # Green background
        fg="#252525",  # White text
        activebackground="#218838",  # Darker green when pressed
        activeforeground="white",  # White text when pressed
        padx=20,
        pady=10,
        state="normal"  # Ensure button is enabled
    )
    confirm_move_button.pack(side="left", padx=10)

    # Resign Button
    resign_button = tk.Button(
        action_frame,
        text="RESIGN",
        font=("Helvetica", 20, "bold"),
        bg="#dc3545",  # Red background
        fg="#252525",  # White text
        activebackground="#c82333",  # Darker red when pressed
        activeforeground="white",  # White text when pressed
        padx=20,
        pady=10,
        state="normal"  # Ensure button is enabled
    )
    resign_button.pack(side="right", padx=10)

    # Load a PGN string into the MoveHistory component
    pgn_string = """[Event "F/S Return Match"]
[Site "Belgrade, Serbia JUG"]
[Date "1992.11.04"]
[Round "29"]
[White "Fischer, Robert J."]
[Black "Spassky, Boris V."]
[Result "1/2-1/2"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3
O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. Nc3 Qc7 13. cxb5 axb5 14. Bg5 h6 15.
Bh4 Re8 16. Rc1 Qb7 17. Bg3 Bf8 18. Qd2 b4 19. Na4 exd4 20. Nxd4 Nxe4 21. Rxe4
Rxe4 22. Nxc6 Nf6 23. Bxd6 Bxd6 24. Qxd6 Bf5 25. Nc5 Qb6 26. Nxe4 Nxe4 27.
Qf4 Bg6 28. Ne5 Nxd6 29. Nxg6 Re8 30. Rc6 Qd4 31. Rxd6 Re1+ 32. Kh2 Qxd6+ 33.
Qxd6 Kh7 34. Nf8+ Kg8 35. Nd7 Re2 36. Kg3 Rxb2 37. Ne5 Kf8 38. Kf3 Ke7 39. Nd3
Rd2 40. Ke3 Rd1 41. Nxb4 Rg1 42. Kf3 Kd6 43. g3 Kc5 44. Nd3+ Kd4 45. Nf4 Re1
46. h4 g5 47. hxg5 hxg5 48. Nh3 f6 49. Kg2 Ke5 50. f4+ gxf4 51. gxf4+ Kf5 52.
Kf3 Rf1+ 53. Ke3 Kg4 54. Nf2+ Kg3 55. Ne4+ Kg4 56. Nxf6+ Kf5 57. Nd5 Re1+ 58.
Kf3 Ra1 59. Ne3+ Kf6 60. Ke4 Ra4+ 61. Kf3 Ke6 62. Kg4 Kf6 63. Nd5+ Ke6 64. Nc7+
Kf6 65. Nd5+ 1/2-1/2"""
    move_history.load_moves(pgn_string)

    # Example function to confirm move
    def confirm_move():
        if move_history.is_current:
            # Add a move manually and update the move history
            move = chess.Move.from_uci("e2e4")
            move_history.board.push(move)
            move_history.update_move_history()
            board_canvas.update_board(move_history.board.fen())
        else:
            # If we're in history mode, reset to current before making a move
            move_history.reset_to_current()
            confirm_move()

    confirm_move_button.config(command=confirm_move)

    # Example function to resign the game
    def resign_game():
        messagebox.showinfo("Resign", "You have resigned the game.")
        game_frame.destroy()
    
        # Import inside the function to avoid circular import
        from home_screen import show_home_screen
        show_home_screen(root)
        
    resign_button.config(command=resign_game)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chess Game")
    root.geometry("1024x768")
    show_game_screen(root, tk.Frame(root), "white", "medium")
    root.mainloop()