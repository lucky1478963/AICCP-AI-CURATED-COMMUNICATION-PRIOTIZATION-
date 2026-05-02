
import streamlit as st


# =====================================
# LOAD CSS SAFELY
# =====================================

try:

    with open(
    "assets/styles.css"
    ) as f:

        st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
        )

except:

    st.warning(
    "CSS file not found"
    )

st.title(
" AICCP (AI CURATED COMMUNICATION PRIOTIZATION)"
)

st.markdown(
"""
<div class="alert-banner">
⚠ CRITICAL SATELLITE ALERT MONITOR ACTIVE
</div>
""",
unsafe_allow_html=True
)

st.success(
"""
AI Communication Curation Platform
Operational
"""
)

st.sidebar.title(
"🛰 Navigation"
)

st.sidebar.success(
"Mission Systems Online"
)

st.info(
"""
Use sidebar to access:
- Dashboard
- Optimizer
- Digital Twin
- Ground Station
- Admin Panel
"""
)
