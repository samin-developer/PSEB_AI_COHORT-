import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("Students from Lahore:", df["city"].eq("Lahore").sum())

top_3 = df.sort_values("score", ascending=False).head(3)
print("\nTop 3 students")
print(top_3.to_string(index=False))

print("\n students that have score 50 or more:", df["score"].ge(50).sum())

df["score"].hist(bins=[40, 50, 60, 70, 80, 90, 100])
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Student Scores")
plt.tight_layout()
plt.show()