def schedule_messages(
messages
):

    messages=sorted(
        messages,
        key=lambda x:x["CPI"],
        reverse=True
    )

    for i,m in enumerate(
        messages,
        start=1
    ):

        m["queue_order"]=i

    return messages



def bandwidth_optimizer(
messages,
limit=2
):

    transmit=messages[:limit]

    defer=messages[limit:]

    return transmit,defer