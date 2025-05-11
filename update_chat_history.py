def save_message_to_json(role, person_name, message):
    file_path = os.path.join(DATA_DIR, f"{person_name}.json")
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(file_path):
        data = {"chat_history": []}
    else:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    if not message.strip():
        return "Empty Message"

    data["chat_history"].append({"role": role, "parts": message})

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return "Message saved"
