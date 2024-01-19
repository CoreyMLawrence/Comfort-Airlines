import mariadb
import sys

def main() -> None:
    """The entry point for the program"""
    print("Hello, Docker!")
    try:
        connection = mariadb.connect(
            user="root",
            password="toor",
            host="192.0.2.1",
            port=3306,
            database="comfort-airlines-db"
        )
        
        cursor = connection.cursor()
        print("Sucessfully connected to the database")
        
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()