import os
def ask_ai(question, documents_folder="uploads"):
    question = question.lower()
    if not os.path.exists(documents_folder):
        return "Koi document abhi tak upload nahi hua."
    found = []
    for f in os.listdir(documents_folder):
        if any(w in f.lower() for w in question.lower().split()):
            found.append(f)
    if found:
        return f"Files mili hain: {', '.join(found)}"
    else:
        return f"'{question}' se related koi file nahi mili, lekin AI kaam kar raha hai."
