from collections import deque
import json

def save_messages(deque_to_list):
    data = list(deque_to_list)
    with open("messages.json", "w") as file:
        json.dump(data, file)

def load_messages():
    try:
        with open("messages.json", "r") as file:
            loaded = json.load(file)
        clean = []
        for item in loaded:
            if isinstance(item, str):
                item_category = classify(item)
                dict_item = {"text": item, "category": item_category}
                clean.append(dict_item)
            else:
                clean.append(item)
        return deque(clean)
    except (FileNotFoundError, json.JSONDecodeError):
        return deque()

def classify(check_txt):
    if "emergency" in check_txt.lower() or "asap" in check_txt.lower():
        category = "Urgent"
    elif "quote" in check_txt.lower() or "price" in check_txt.lower():
        category = "Sales"
    else:
        category = "General"

    return category

messages = load_messages()

def add(queue, message, text_category):
    if message == "":
        print("Empty message")
    else:
        text_dict = {"text": message, "category": text_category}
        queue.append(text_dict)

def view(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        for message1 in queue:
            print(f"{message1['text']} - {message1['category']}")

def process(queue):
    if len(queue) == 0:
        print("Nothing to process")
    else:
        first = queue.popleft()
        print(f"{first['text']} - {first['category']}")

running = True
while running:
    choice = str(input("What do you want to do? (add, view, process, quit) "))
    if choice.lower() == "add":
        text = str(input("Enter a message: "))
        new_text_category = classify(text)
        add(messages, text, new_text_category)

    elif choice.lower() == "view":
        view(messages)

    elif choice.lower() == "process":
        process(messages)

    elif choice.lower() == "quit":
        save_messages(messages)
        print("Goodbye Soldier")
        running = False

    else:
        print("Invalid choice")