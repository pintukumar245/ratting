import random
import csv

# Only the sentiments/emotions from the PDF
positive_feedbacks = [
    "Excellent Mentor",
    "Very Helpful",
    "Good Guidance",
    "Great Support",
    "Wonderful Teaching",
    "Outstanding Help",
    "Brilliant Mentor",
    "Superb Guidance",
    "Highly Recommended",
    "Fantastic Sessions",
    "Very Knowledgeable",
    "Exceptional Mentor",
    "Impressive Teaching",
    "Remarkable Guidance",
    "Excellent Support",
]

neutral_feedbacks = [
    "Average Session",
    "Decent Guidance",
    "Okay Mentor",
    "Moderate Help",
    "Fair Teaching",
    "Satisfactory Session",
    "Acceptable Guidance",
    "Average Support",
    "Ordinary Session",
    "So So Mentor",
]

negative_feedbacks = [
    "Needs Improvement",
    "Poor Guidance",
    "Not Helpful",
    "Disappointing Session",
    "Below Average Mentor",
    "Unsatisfactory Help",
    "Lacks Clarity",
    "Poor Communication",
    "Not Recommended",
    "Very Poor Session",
]

all_feedbacks = positive_feedbacks + neutral_feedbacks + negative_feedbacks

# 40 mentors
mentor_ids = [f"MT{100 + i}" for i in range(1, 41)]

rows = []
for _ in range(500):
    mentor_id = random.choice(mentor_ids)
    feedback_text = random.choice(all_feedbacks)
    rows.append([mentor_id, feedback_text])

output_path = "synthetic_feedback.csv"  # saves in the same folder as your .py file
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["mentor_id", "feedback_text"])
    writer.writerows(rows)

print(f"CSV generated: {output_path}")
print(f"Total rows: {len(rows)}")
print(f"Unique mentors in data: {len(set(r[0] for r in rows))}")