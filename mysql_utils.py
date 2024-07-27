import os
import mysql.connector

def get_top_universities(keyword):
    try:
        # Connect to the MySQL database using environment variables
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'test_root'),
            database=os.getenv('MYSQL_DB', 'academicworld')
        )
        cursor = connection.cursor()

        # Define the prepared statement
        query = """
        SELECT u.name AS university_name, COUNT(p.ID) AS publication_count
        FROM publication p
        JOIN publication_keyword pk ON p.ID = pk.publication_id
        JOIN keyword k ON pk.keyword_id = k.id
        JOIN faculty_publication fp ON p.ID = fp.publication_id
        JOIN faculty f ON fp.faculty_id = f.id
        JOIN university u ON f.university_id = u.id
        WHERE k.name = %s
        GROUP BY u.name
        ORDER BY publication_count DESC
        LIMIT 10;
        """

        # Execute the prepared statement
        cursor.execute(query, (keyword,))
        results = cursor.fetchall()

        # Close the connection
        cursor.close()
        connection.close()

        return results
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
