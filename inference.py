def run(input_data):
    try:
        # Extract email text safely
        email = input_data.get("email", "").lower()

        if any(word in email for word in ["urgent", "asap", "immediately"]):
            return {"priority": "high", "category": "urgent"}

        elif any(word in email for word in ["meeting", "schedule", "call"]):
            return {"priority": "medium", "category": "meeting"}

        elif any(word in email for word in ["offer", "discount", "sale"]):
            return {"priority": "low", "category": "promotion"}

        else:
            return {"priority": "low", "category": "general"}

    except Exception as e:
        return {"error": str(e)}