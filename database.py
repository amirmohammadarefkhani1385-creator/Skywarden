

"""SQLite storage for the astronomy observation ."""


def save_observations_to_db(observations, connection):
    """Save a list of observations into the observations table.

    The table is created automatically if it does not exist yet.

    Args:
        observations: List of Observation objects to store.
        connection: An open sqlite3 connection.
    """
    if not observations:
        print("\n  Nothing to save yet.")
        return

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            observer TEXT,
            filter_name TEXT,
            exposure_seconds REAL
        )
    """)

    for observation in observations:
        cursor.execute(
            """
            INSERT INTO observations (target, observer, filter_name, exposure_seconds)
            VALUES (?, ?, ?, ?)
            """,
            (
                observation.target,
                observation.observer,
                observation.filter_name,
                observation.exposure_seconds,
            ),
        )

    connection.commit()
    print(f"\n  {len(observations)} observation(s) saved to the database.")





