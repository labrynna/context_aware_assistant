def analyze_chat_for_meetup(chat_history):
    latest_message = chat_history[-1]["parts"].strip()
    prompt = f"""
    Determine if the latest message suggests a meetup.
    Extract date, time, and location if present.

    Chat History:
    {chat_history}

    Latest Message:
    {latest_message}

    Response Format (JSON):
    {{
        "meetup": "yes" or "no",
        "date": "YYYY-MM-DD",
        "time": "HH:MM",
        "location": "..."
    }}
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    cleaned_text = clean_gemini_response(response.text.strip())
    return json.loads(cleaned_text)
