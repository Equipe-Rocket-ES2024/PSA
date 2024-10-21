from src.game.game import Game

if __name__ == "__main__":
    game = Game()
    
    if game.menu_inicial():
        game.run_game()
