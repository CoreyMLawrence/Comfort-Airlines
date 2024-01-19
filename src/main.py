import mariadb
import sys

DATABASE_USERNAME="root"
DATABASE_PASSWORD="toor"
DATABASE_IP="172.17.0.1"
DATABASE_PORT=3306
DATABASE_NAME="comfort-airlines-db"


def main() -> None:
    """The entry point for the program"""
    print("Hello, Docker!")
    try:
        connection = mariadb.connect(
            user=DATABASE_USERNAME,
            password=DATABASE_PASSWORD,
            host=DATABASE_IP,
            port=DATABASE_PORT,
            database=DATABASE_NAME
        )
        
        cursor = connection.cursor()
        print("Sucessfully connected to the database")
        
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()