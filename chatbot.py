# chatbot.py

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "balance" in user_input:
        return "Your current account balance is ₹56,000."
    elif "transfer" in user_input:
        return "To transfer funds, please provide recipient account number and amount."
    elif "open account" in user_input:
        return "Sure, you can open an account by visiting the nearest branch or our website."
    elif "loan" in user_input:
        return "We offer personal, home, and car loans. What kind of loan are you interested in?"
    elif "credit card" in user_input:
        return "We have several credit cards. Would you like cashback or travel rewards?"
    elif "help" in user_input:
        return "I can help you with account balance, fund transfers, loans, and card services."
    else:
        return "Sorry, I didn't understand that. Can you rephrase your question?"
