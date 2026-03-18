import json

MEMORY_FILE = "data/memory.json"


def load_memory():

    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def add_memory(user, message):

    memory = load_memory()

    if user not in memory:
        memory[user] = []

    memory[user].append(message)

    save_memory(memory)


def get_memory(user):

    memory = load_memory()

    return memory.get(user, [])