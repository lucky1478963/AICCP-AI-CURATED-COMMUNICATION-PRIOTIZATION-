
import mysql.connector


def save_event(
event_name,
department,
priority
):

    try:

        db=mysql.connector.connect(

        host="localhost",
        user="root",
        password="Lucky@1478963",
        database="aiccp"

        )

        cursor=db.cursor()

        sql="""
        INSERT INTO mission_events
        (
        event_name,
        department,
        priority
        )
        VALUES
        (%s,%s,%s)
        """

        values=(
        event_name,
        department,
        priority
        )

        cursor.execute(
        sql,
        values
        )

        db.commit()

        db.close()

        return True

    except Exception as e:

        print(e)

        return False

