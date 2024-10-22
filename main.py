from src.game.game import Game

if __name__ == "__main__":
    game = Game()
    
    if game.initial_menu():
        game.run_game()
