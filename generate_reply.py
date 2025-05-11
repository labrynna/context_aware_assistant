def generate_reply(contact_name, message):
    instructions = load_instructions(contact_name)
    chat_history = load_chat_history(contact_name)["chat_history"]

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=instructions,
        generation_config={
            "temperature": 0,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192
        },
        safety_settings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ]
    )

    chat_session = model.start_chat(history=chat_history)
    response = chat_session.send_message(message)
    reply = re.sub(r'[^
