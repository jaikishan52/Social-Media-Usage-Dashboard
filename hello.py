import pandas as pd
import plotly.express as px
import preswald

# 1. Load your dataset
df = pd.read_csv("data/Students Social Media Addiction.csv")

# 2. Create a scatter plot: Age vs. Usage
fig = px.scatter(
    df,
    x="Age",
    y="Avg_Daily_Usage_Hours",
    color="Gender",
    hover_data=["Addicted_Score"],
    title="Age vs. Daily Social Media Usage",
    labels={
        "Age": "Age (years)",
        "Avg_Daily_Usage_Hours": "Daily Usage (hours)"
    }
)
fig.update_traces(marker=dict(size=12, opacity=0.7))
fig.update_layout(template="plotly_white")


# 3. Style the plot
fig.update_traces(marker=dict(size=12, opacity=0.7))

fig.update_layout(template="plotly_white")

# 4. Display in Preswald
preswald.text("# Social Media Usage Dashboard")
preswald.text("This dashboard analyzes how student age relates to their average daily social media use.")
preswald.plotly(fig)
preswald.table(df)
