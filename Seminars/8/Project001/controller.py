import view
import model
import logger

def run_calc():
    mode = view.choose_mode()
    if mode == 1:
        expr = view.get_expr(mode)
        result = model.get_result(expr, mode)
        view.show_result(expr, result, mode)
        logger.log_result(expr, result, mode)
    elif mode == 2:
        expr = view.get_expr(mode)
        result = model.get_result(expr, mode)
        view.show_result(expr, result, mode)
        logger.log_result(expr, result, mode)
    elif mode == 3:
        expr = view.get_expr(mode)
        result = model.get_result(expr, mode)
        view.show_result(expr, result, mode)
        logger.log_result(expr, result, mode)
    else: 
        view.error_mode()


