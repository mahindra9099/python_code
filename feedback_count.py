# collection user feedback
feedback = ["Great service!", "Very satisfied","could be better","Excellent experience"]

# adding new feedback
feedback.append("Not happy with the service")

# counting specific feedback

feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())

print(feedback_count)