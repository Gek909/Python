import game1
import game2
import view
import logger

def run():
    mode = view.choose_mode()
    if mode == 1:
        result = game1.run_game()
        view.show_result(result)
        logger.log_result(mode, result)
    if mode == 2:
        result = game2.run_game()
        view.show_result(result)
        logger.log_result(mode, result)
            