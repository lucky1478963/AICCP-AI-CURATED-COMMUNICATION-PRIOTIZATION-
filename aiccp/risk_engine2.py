def calculate_risk(
severity,
urgency,
criticality
):

    risk=(
0.5*severity+
0.3*urgency+
0.2*criticality
)

    return round(risk,2)



def assign_priority(risk):

    if risk>=8:
        return "CRITICAL"

    elif risk>=6:
        return "HIGH"

    elif risk>=4:
        return "MEDIUM"

    else:
        return "LOW"