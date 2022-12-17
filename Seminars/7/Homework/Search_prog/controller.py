import logger
import model
import view

def run():
    mode = view.choose_mode()
    if mode == 1:
        object = view.get_object(mode)
        base = logger.get_data()
        results = model.find_contact(object, base)
        view.show_result(results, base)
    if mode == 2:
        object = view.get_object(mode)
        model.create_contact(object)
        view.sucсessfullly_added(object)