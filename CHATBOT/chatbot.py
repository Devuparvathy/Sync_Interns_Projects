def health_remedies_bot(user_input):
    user_input_lower = user_input.lower()

    if "headache" in user_input_lower:
        return "For a headache, try drinking plenty of water, resting in a dark room, and using a cold or warm compress on your forehead."

    elif "sore throat" in user_input_lower:
        return "For a sore throat, consider gargling with warm saltwater, drinking herbal tea with honey, and staying hydrated."

    elif "cold" in user_input_lower or "flu" in user_input_lower:
        return "For a cold or flu, get plenty of rest, stay hydrated, and consider over-the-counter remedies for symptom relief."

    elif "stomachache" in user_input_lower or "indigestion" in user_input_lower:
        return "For a stomachache or indigestion, try sipping on ginger tea, avoiding heavy meals, and taking a short walk."

    elif (
        "thanks" in user_input_lower
        or "okay" in user_input_lower
        or "ok" in user_input_lower
    ):
        return "It's my pleasure to help you! Feel free to ask if you need more information."

    elif any(greeting in user_input_lower for greeting in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"

    else:
        return "I'm not a doctor, and these remedies are general suggestions. For serious health concerns, please consult with a healthcare professional."


def health_remedies_chatbot():
    print(
        "Hello! I'm your health remedies chatbot. Type 'exit' to end the conversation."
    )

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = health_remedies_bot(user_input)
        print(f"Bot: {response}")


health_remedies_chatbot()
