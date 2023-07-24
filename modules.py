import pickle


def load_tasks():
    try:
        with open("tasks.pickle", 'rb') as file:
            loaded_tasks = pickle.load(file)
            return loaded_tasks
    except:
        with open("tasks.pickle", 'wb') as file:
            pickle.dump([], file)
        return []


def save_task(list_to_save):
    with open("tasks.pickle", 'wb') as file:
        pickle.dump(list_to_save, file)


def remove_all_tasks():
    with open("tasks.pickle", 'wb') as file:
        pickle.dump([], file)
        print()
        print("All Tasks Removed")
    return []
