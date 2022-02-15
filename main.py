import sys
import pandas as pd
import plotly.graph_objects as go


def display_plot(results_csv: str):
    df = pd.read_csv(results_csv or "results.csv")
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


if __name__ == "__main__":
    results_file = sys.argv[1] if len(sys.argv) > 1 else None
    display_plot(results_file)
