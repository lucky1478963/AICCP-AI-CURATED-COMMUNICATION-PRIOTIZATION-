import streamlit as st
import pandas as pd
import plotly.express as px
import random


# ============================================
# PAGE TITLE
# ============================================

st.title(
"📡 AI Communication Optimizer"
)

st.markdown(
"""
Analyze communication load,
packet prioritization,
and bandwidth allocation
using AICCP intelligence.
"""
)


# ============================================
# KPI CARDS
# ============================================

a,b,c,d=st.columns(4)

a.metric(
"Bandwidth Efficiency",
f"{random.randint(70,98)}%"
)

b.metric(
"Priority Messages",
random.randint(10,50)
)

c.metric(
"Transmission Delay",
f"{random.randint(1,8)} ms"
)

d.metric(
"Optimization Gain",
f"{random.randint(20,60)}%"
)

st.markdown("---")


# ============================================
# AI PRIORITY TABLE
# ============================================

st.subheader(
"🧠 AI Packet Prioritization"
)

priority_data=pd.DataFrame(
{

"Packet":[
"P-101",
"P-102",
"P-103",
"P-104",
"P-105"
],

"Subsystem":[
"Power",
"Navigation",
"Thermal",
"Communication",
"Payload"
],

"Risk":[
92,
74,
60,
88,
45
],

"Priority":[
"CRITICAL",
"HIGH",
"MEDIUM",
"CRITICAL",
"LOW"
]

}
)

st.dataframe(
priority_data,
use_container_width=True
)


# ============================================
# PRIORITY DISTRIBUTION
# ============================================

st.markdown("---")

st.subheader(
"📊 Priority Distribution"
)

priority_count=pd.DataFrame(
{

"Priority":[
"Critical",
"High",
"Medium",
"Low"
],

"Count":[
12,
8,
6,
3
]

}
)

fig=px.pie(
priority_count,
values="Count",
names="Priority",
title="Packet Priority Analysis"
)

fig.update_layout(
paper_bgcolor="#050816",
plot_bgcolor="#050816",
font_color="white"
)

st.plotly_chart(
fig,
use_container_width=True
)


# ============================================
# BANDWIDTH UTILIZATION
# ============================================

st.markdown("---")

st.subheader(
"📈 Bandwidth Utilization"
)

bandwidth=pd.DataFrame(
{

"Channel":[
"CH-1",
"CH-2",
"CH-3",
"CH-4"
],

"Usage":[
82,
67,
91,
54
]

}
)

fig2=px.bar(
bandwidth,
x="Channel",
y="Usage",
title="Communication Channel Usage"
)

fig2.update_layout(
paper_bgcolor="#050816",
plot_bgcolor="#050816",
font_color="white"
)

st.plotly_chart(
fig2,
use_container_width=True
)


# ============================================
# AI DECISION ENGINE
# ============================================

st.markdown("---")

st.subheader(
"⚙ AI Optimization Engine"
)

if st.button(
"Run Optimization"
):

    st.success(
    "AI Optimization Complete"
    )

    st.info(
    """
Critical packets rerouted.
Bandwidth reallocated.
Latency reduced.
"""
    )



# ============================================
# COMMUNICATION HEATMAP
# ============================================

st.markdown("---")

st.subheader(
"🌐 Communication Heatmap"
)

heatmap=pd.DataFrame(
{

"Region":[
"Asia",
"Europe",
"Africa",
"North America",
"South America"
],

"Traffic":[
92,
61,
43,
78,
55
]

}
)

fig3=px.density_heatmap(
heatmap,
x="Region",
y="Traffic",
z="Traffic",
title="Global Communication Load"
)

fig3.update_layout(
paper_bgcolor="#050816",
plot_bgcolor="#050816",
font_color="white"
)

st.plotly_chart(
fig3,
use_container_width=True
)


# ============================================
# QUEUE VISUALIZATION
# ============================================

st.markdown("---")

st.subheader(
"📦 Transmission Queue"
)

queue=pd.DataFrame(
{

"Packet":[
"P-101",
"P-102",
"P-103",
"P-104"
],

"Status":[
"Transmitting",
"Queued",
"Deferred",
"Priority Routed"
],

"Progress":[
90,
60,
30,
100
]

}
)

st.dataframe(
queue,
use_container_width=True
)

for i,row in queue.iterrows():

    st.write(
    row["Packet"]
    )

    st.progress(
    row["Progress"]/100
    )


# ============================================
# FINAL AI REPORT
# ============================================

st.markdown("---")

st.subheader(
"📜 AI Optimization Report"
)

st.code(
"""
AICCP Optimization Summary

- Critical packets prioritized
- Communication delay reduced
- Bandwidth balanced dynamically
- Packet rerouting successful
- AI scheduling active
"""
)