def generate_spacecraft_state(
scenario
):

    if scenario=="Normal":

        return {
        "Power":95,
        "Thermal":90,
        "Navigation":92,
        "Communication":94
        }


    elif scenario=="Power Failure":

        return {
        "Power":42,
        "Thermal":60,
        "Navigation":80,
        "Communication":76
        }


    elif scenario=="Solar Storm":

        return {
        "Power":70,
        "Thermal":55,
        "Navigation":65,
        "Communication":50
        }

    else:

        return {
        "Power":80,
        "Thermal":78,
        "Navigation":75,
        "Communication":40
        }



def fault_propagation(
state
):

    effects=[]


    if state["Power"]<60:

        effects.append(
"Thermal instability risk"
)

        effects.append(
"Communication degradation"
)


    return effects