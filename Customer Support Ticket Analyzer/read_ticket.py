import pandas as pd
from support_ticket_class import Status,Priority
# Read the dataset.
df = pd.read_csv("tickets.csv")
print(df)
# Read the dataset.

# Find total tickets.
print(f"total tickets:{len(df)} ")
# Count tickets by category.
#print(f"tickets by category: {df.groupby("category")["ticket_id"].count()}")
print(f"tickets by category: {df.groupby("category").value_counts()}")
# Count tickets by priority.
print(f"tickets by priority: {df.groupby("priority").value_counts()}")
# Count tickets by status.
print(f"tickets by status: {df.groupby("status").value_counts()}")
# Find open tickets.
print(f"open tickets: {df[df["status"]==Status.OPEN]}")
# Find critical tickets.
print(f"critical tickets: {df[df["priority"]==Priority.CRITICAL]}")
# Find resolved tickets.
print(f"resolved tickets: {df[df["status"]==Status.RESOLVED]}")
# Find average resolution time.
print(f"average resolution time: {df["resolution_time"].mean()}")
# Find average resolution time per category.
print(f"average resolution time per category: {df.groupby("category")["resolution_time"].mean()}")
# Find tickets handled by each support agent.
print(f"tickets handled by each support agent: {df["assigned_agent"].value_counts()}")
# Sort tickets by resolution time.
print(f" Sort tickets by resolution time: {df.sort_values("resolution_time",ascending=True)}")
# Find tickets taking maximum resolution time.
print(f"Find tickets taking maximum resolution time: {df[df["resolution_time"] == df["resolution_time"].max()]}")

# Export summary report.


# -----------------------------
# 1. Category Summary
# -----------------------------
category_summary = (
    df["category"]
    .value_counts()
    .reset_index()
)

category_summary.columns = ["category", "ticket_count"]


# -----------------------------
# 2. Agent Summary
# -----------------------------
agent_summary = (
    df.groupby("assigned_agent")
    .agg(
        ticket_count=("ticket_id", "count"),
        average_resolution_time=("resolution_time", "mean"),
        maximum_resolution_time=("resolution_time", "max")
    )
    .reset_index()
)


# -----------------------------
# 3. Status Summary
# -----------------------------
status_summary = (
    df["status"]
    .value_counts()
    .reset_index()
)

status_summary.columns = ["status", "ticket_count"]


# -----------------------------
# 4. Priority Summary
# -----------------------------
priority_summary = (
    df["priority"]
    .value_counts()
    .reset_index()
)

priority_summary.columns = ["priority", "ticket_count"]


# -----------------------------
# Export reports
# -----------------------------

category_summary.to_csv("category_summary.csv", index=False)
agent_summary.to_csv("agent_summary.csv", index=False)
status_summary.to_csv("status_summary.csv", index=False)
priority_summary.to_csv("priority_summary.csv", index=False)


print("Summary reports exported successfully!")
