import pandas as pd
import plotly.graph_objects as go

# Replace results.csv with your results file
df = pd.read_csv("results.csv")
df["TEST ID"] = [x for x in range(0, len(df))]

fig = go.Figure(
    data=[
        go.Bar(
            name="Qualiti Scripts Duraction (ms)",
            x=df["TEST ID"],
            y=df["QUALITI SCRIPTS DURATION"],
        ),
        go.Bar(
            name="First Contentful Paint (ms)",
            x=df["TEST ID"],
            y=df["FIRST CONTENTFUL PAINT"],
        ),
        go.Bar(name="Page Load Time (ms)", x=df["TEST ID"], y=df["PAGE LOAD TIME"]),
    ]
)

fig.update_layout(barmode="group", title_text="Web Performance Metrics")
fig.show()
