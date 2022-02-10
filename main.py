import pandas as pd
import plotly.graph_objects as go

# Replace results.csv with your results file
df = pd.read_csv("results.csv")
df["TEST ID"] = [x for x in range(0, len(df))]

fig = go.Figure(
    data=[
        go.Bar(
            name="Page Load Time (ms)",
            x=df["TEST ID"],
            y=df["PAGE LOAD TIME (ms)"],
        ),
        go.Bar(
            name="Qualiti Scripts Duration (ms)",
            x=df["TEST ID"],
            y=df["SCRIPT DURATION (ms)"],
        ),
    ]
)

# Change the bar mode
fig.update_layout(barmode="group", title_text="Web Performance Metrics")
fig.show()
