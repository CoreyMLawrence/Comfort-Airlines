import pytest
import mariadb
import os

def test_db_connection() -> None:
    pass
#        connection = mariadb.connect(
#            user=os.environ["DATABASE_USERNAME"],
#            password=os.environ["DATABASE_PASSWORD"],
#            host=os.environ["DATABASE_IP"],
#            port=int(os.environ["DATABASE_PORT"]),
#            database=os.environ["DATABASE_NAME"]
#        )
