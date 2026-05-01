import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time


# ============================================
# PAGE TITLE
# ============================================

st.title(
"🧠 Digital Twin Intelligence System"
)

st.markdown(
"""
AI-driven spacecraft simulation,
fault propagation analysis,
and predictive anomaly detection.
"""
)


# ============================================
# SYSTEM STATUS
# ============================================

st.markdown(
"""
<div class="alert-banner">
DIGITAL TWIN SYNCHRONIZED
</div>
""",
unsafe_allow_html=True
)


# ============================================
# KPI CARDS
# ============================================

a,b,c,d=st.columns(4)

a.metric(
"Subsystems Active",
8
)

b.metric(
"Anomalies Detected",
random.randint(1,6)
)

c.metric(
"Prediction Accuracy",
f"{random.randint(85,99)}%"
)

d.metric(
"AI Recovery Confidence",
f"{random.randint(70,98)}%"
)

st.markdown("---")


# ============================================
# SPACECRAFT HEALTH
# ============================================

st.subheader(
"🛰 Spacecraft Subsystem Health"
)

systems=pd.DataFrame(
{

"Subsystem":[
"Power",
"Thermal",
"Navigation",
"Communication",
"Payload",
"Battery",
"Processor",
"Propulsion"
],

"Health":[
92,
74,
81,
69,
88,
58,
76,
83
]

}
)

st.dataframe(
systems,
use_container_width=True
)


# ============================================
# HEALTH CHART
# ============================================

fig=px.bar(
systems,
x="Subsystem",
y="Health",
color="Health",
title="Subsystem Health Monitoring"
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
# LIVE ANOMALY DETECTION
# ============================================

st.markdown("---")

st.subheader(
"⚠ Live Anomaly Detection"
)

anomalies=[
"Thermal fluctuation detected",
"Battery instability detected",
"Navigation drift identified",
"Communication packet loss",
"Solar radiation spike"
]

selected=random.choice(
anomalies
)

st.error(
selected
)

risk=random.randint(70,98)

st.warning(
f"Predicted Mission Risk: {risk}%"
)

st.info(
"AI recovery protocol recommended"
)


# ============================================
# FAULT PROPAGATION
# ============================================

st.markdown("---")

st.subheader(
"🔄 Fault Propagation Analysis"
)

propagation=pd.DataFrame(
{

"Fault Source":[
"Battery",
"Thermal",
"Communication"
],

"Affected System":[
"Power Grid",
"Processor",
"Navigation"
],

"Impact":[
"High",
"Medium",
"Critical"
]

}
)

st.dataframe(
propagation,
use_container_width=True
)


# ============================================
# DIGITAL TWIN TREND
# ============================================

st.markdown("---")

st.subheader(
"📈 Predictive Failure Trend"
)

trend=pd.DataFrame(
{

"Time":[1,2,3,4,5,6,7],

"Failure Probability":[
20,
28,
35,
49,
61,
74,
88
]

}
)

fig2=px.line(
trend,
x="Time",
y="Failure Probability",
markers=True,
title="AI Failure Prediction"
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
# RECOVERY ENGINE
# ============================================

st.markdown("---")

st.subheader(
"🛠 AI Recovery Recommendation Engine"
)

recommendations=[
"Switch to backup communication link",
"Reduce thermal load immediately",
"Activate secondary power routing",
"Recalibrate navigation subsystem",
"Prioritize emergency telemetry"
]

for r in recommendations:

    st.success(r)


# ============================================
# DIGITAL TWIN SIMULATION
# ============================================

st.markdown("---")

st.subheader(
"🌌 Live Spacecraft Simulation"
)

simulation=pd.DataFrame(
{

"Module":[
"Power",
"Thermal",
"Navigation",
"Communication"
],

"Simulation State":[
"Stable",
"Warning",
"Stable",
"Critical"
]

}
)

st.dataframe(
simulation,
use_container_width=True
)


# ============================================
# AI DECISION LOGS
# ============================================

st.markdown("---")

st.subheader(
"📜 AI Decision Logs"
)

st.code(
"""
[09:21] Digital twin synchronized
[09:22] Thermal anomaly predicted
[09:23] AI recovery protocol initiated
[09:24] Backup communication activated
[09:25] Failure probability escalated
"""
)


# ============================================
# FINAL REPORT
# ============================================

st.markdown("---")

st.subheader(
"📄 Digital Twin Analysis Report"
)

st.info(
"""
AICCP digital twin continuously
simulates spacecraft health,
predicts subsystem degradation,
and assists mission recovery
using AI-assisted anomaly detection.
"""
)