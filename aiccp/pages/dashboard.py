
import streamlit as st
import pandas as pd
import random
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

from aws_alert import send_critical_alert


# =====================================
# AUTO REFRESH
# =====================================

st_autorefresh(
    interval=3000,
    key="telemetry_refresh"
)


# =====================================
# PAGE TITLE
# =====================================

st.title(
    "🛰 AICCP Mission Control Dashboard"
)

st.markdown(
    """
    <div class="alert-banner">
    🚀 LIVE SATELLITE OPERATIONS ACTIVE
    </div>
    """,
    unsafe_allow_html=True
)


# =====================================
# KPI CARDS
# =====================================

a, b, c, d = st.columns(4)

a.metric(
    "Mission Risk",
    f"{random.randint(60,90)}%"
)

b.metric(
    "Bandwidth Usage",
    f"{random.randint(50,95)}%"
)

c.metric(
    "Queued Packets",
    random.randint(5,20)
)

d.metric(
    "AI Decisions",
    random.randint(200,500)
)

st.markdown("---")


# =====================================
# SATELLITE CONSTELLATION
# =====================================

st.subheader(
    "🛰 Satellite Constellation"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div style="
        background:#0f172a;
        padding:20px;
        border-radius:20px;
        border:1px solid #38bdf8;
        text-align:center;
        ">
        <h2>🛰 SAT-A</h2>
        <h3 style='color:lime'>
        HEALTHY
        </h3>
        <p>Health: 92%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div style="
        background:#0f172a;
        padding:20px;
        border-radius:20px;
        border:1px solid orange;
        text-align:center;
        ">
        <h2>🛰 SAT-B</h2>
        <h3 style='color:orange'>
        WARNING
        </h3>
        <p>Health: 64%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div style="
        background:#0f172a;
        padding:20px;
        border-radius:20px;
        border:1px solid red;
        text-align:center;
        ">
        <h2>🛰 SAT-C</h2>
        <h3 style='color:red'>
        CRITICAL
        </h3>
        <p>Health: 38%</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================
# LIVE TELEMETRY
# =====================================

st.markdown("---")

st.subheader(
    "📡 Live Telemetry"
)

telemetry = pd.DataFrame(
    {

        "Subsystem":[
            "Power",
            "Thermal",
            "Navigation",
            "Communication"
        ],

        "Telemetry":[
            random.randint(40,100),
            random.randint(40,100),
            random.randint(40,100),
            random.randint(40,100)
        ]

    }
)

st.dataframe(
    telemetry,
    use_container_width=True
)


# =====================================
# TELEMETRY CHART
# =====================================

fig = px.bar(
    telemetry,
    x="Subsystem",
    y="Telemetry",
    title="Subsystem Telemetry"
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


# =====================================
# PACKET FLOW
# =====================================

st.markdown("---")

st.subheader(
    "📦 Packet Transmission Flow"
)

packets = {

    "P-101":90,
    "P-102":65,
    "P-103":40,
    "P-104":100

}

for packet, progress in packets.items():

    st.write(packet)

    st.progress(
        progress/100
    )


# =====================================
# DIGITAL TWIN TREND
# =====================================

st.markdown("---")

st.subheader(
    "🧠 Digital Twin Prediction"
)

trend = pd.DataFrame(
    {

        "Time":[1,2,3,4,5,6],

        "Risk":[
            20,
            35,
            48,
            62,
            75,
            89
        ]

    }
)

fig2 = px.line(
    trend,
    x="Time",
    y="Risk",
    markers=True,
    title="Predicted Failure Escalation"
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


# =====================================
# FAULT INJECTION
# =====================================

st.markdown("---")

st.subheader(
    "⚠ Fault Injection System"
)

fault = st.selectbox(
    "Select Fault",
    [
        "Solar Storm",
        "Battery Failure",
        "Thermal Spike",
        "Communication Blackout"
    ]
)

if st.button(
    "Inject Fault"
):

    risk = random.randint(75,99)

    st.error(
        f"{fault} detected"
    )

    st.warning(
        f"Mission Risk Elevated to {risk}%"
    )

    st.info(
        "AI Recovery Protocol Activated"
    )

    # =================================
    # SEND AWS EMAIL ALERT
    # =================================

    email_result = send_critical_alert(
        fault,
        risk
    )

    if email_result:

        st.success(
            "AWS SES Email Alert Sent"
        )

    else:

        st.error(
            "Email sending failed"
        )

    # =================================
    # ALERT BANNER
    # =================================

    st.markdown(
        """
        <div class="alert-banner">
        🚨 CRITICAL SATELLITE ALERT ESCALATED
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================
# MISSION LOGS
# =====================================

st.markdown("---")

st.subheader(
    "📜 Mission Activity Logs"
)

st.code(
    """
[09:21] Satellite anomaly detected
[09:22] AI elevated communication priority
[09:23] Packet rerouting activated
[09:24] Digital twin synchronized
[09:25] AWS SES alert dispatched
"""
)
