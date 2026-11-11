
import os
import psycopg2
import dotenv

dotenv.load_dotenv()


def get_books_by_author(author_name: str) -> None:

    # Step 1: Connect to PostgreSQL
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
    )

    try:
        # Step 2: Create cursor
        cur = conn.cursor()

        # Step 3: Write SQL query
        query = """
            SELECT b.title, a.name FROM books b
            JOIN authors a ON b.author_id = a.id
            WHERE a.name = %s;
        """

        # Step 4: Execute parameterized query
        cur.execute(query, (author_name,))

        # Step 5: Fetch results
        results = cur.fetchall()

        # Step 6: Display results
        if results:
            for row in results:
                print(row)
        else:
            print("No books found for this author.")

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":

    author = input("Enter author name: ")

    get_books_by_author(author)
