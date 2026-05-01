
import boto3


def send_critical_alert(

fault_name,
risk_level

):

    try:

        ses=boto3.client(
        "ses",
        region_name="ap-south-1"
        )

        response=ses.send_email(

        Source="sahoobiswapratap663@gmail.com",

        Destination={
        "ToAddresses":[
        "sahoobiswapratap663@gmail.com"
        ]
        },

        Message={

        "Subject":{
        "Data":"🚨 AICCP Critical Satellite Alert"
        },

        "Body":{

        "Text":{

        "Data":f"""

AICCP ENTERPRISE ALERT

Critical Fault Detected

Fault:
{fault_name}

Risk Level:
{risk_level}%

AI Recovery Protocol Activated.

Mission Control Action Required.

"""
        }

        }

        }

        )

        print(
        "EMAIL SENT"
        )

        return True

    except Exception as e:

        print(e)

        return False

