def compute_cpi(
risk,
information,
mission
):

    cpi=(
0.5*risk+
0.3*information+
0.2*mission
)

    return round(
cpi,
2
)



def curate_action(
cpi
):

    if cpi>=8:
        return "Transmit Immediately"

    elif cpi>=6:
        return "High Priority Queue"

    elif cpi>=4:
        return "Delay Transmission"

    else:
        return "Defer"