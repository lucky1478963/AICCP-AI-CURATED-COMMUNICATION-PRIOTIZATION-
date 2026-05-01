def predict_failure(
state
):

    power=state["Power"]

    probability=max(
0,
100-power+15
)


    if probability>60:

        rec="Immediate diagnostics"

    else:

        rec="Continue monitoring"


    return probability,rec