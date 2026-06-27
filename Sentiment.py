import pandas as pd

# Load your generated CSV
df = pd.read_csv("synthetic_feedback.csv")

# Mapping feedback text to sentiment
positive_feedbacks = [
    "Excellent Mentor", "Very Helpful", "Good Guidance", "Great Support",
    "Wonderful Teaching", "Outstanding Help", "Brilliant Mentor", "Superb Guidance",
    "Highly Recommended", "Fantastic Sessions", "Very Knowledgeable",
    "Exceptional Mentor", "Impressive Teaching", "Remarkable Guidance", "Excellent Support"
]

neutral_feedbacks = [
    "Average Session", "Decent Guidance", "Okay Mentor", "Moderate Help",
    "Fair Teaching", "Satisfactory Session", "Acceptable Guidance",
    "Average Support", "Ordinary Session", "So So Mentor"
]

negative_feedbacks = [
    "Needs Improvement", "Poor Guidance", "Not Helpful", "Disappointing Session",
    "Below Average Mentor", "Unsatisfactory Help", "Lacks Clarity",
    "Poor Communication", "Not Recommended", "Very Poor Session"
]

# Function to assign sentiment
def get_sentiment(text):
    if text in positive_feedbacks:
        return "Positive"
    elif text in neutral_feedbacks:
        return "Neutral"
    elif text in negative_feedbacks:
        return "Negative"
    else:
        return "Unknown"

# Add sentiment column
df["sentiment"] = df["feedback_text"].apply(get_sentiment)

# Save updated CSV
df.to_csv("synthetic_feedback.csv", index=False)

print(df.head(10))
print("\nSentiment counts:")
print(df["sentiment"].value_counts())




# Step 2: Convert Sentiment to Score
score_map = {
    "Positive": 5,
    "Neutral": 3,
    "Negative": 1
}

df["score"] = df["sentiment"].map(score_map)

# Save final CSV
df.to_csv("synthetic_feedback.csv", index=False)

print(df.head(10))
print("\nScore counts:")
print(df["score"].value_counts())