from mysql.connector import connect, Error

connection = None

try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="monitoring_db",
        port="3306"
    )
    
    cursor = connection.cursor()
    print("Connected to the database!")

    def checkUser(username, password=None):
        cmd = f"Select count(username) from users where username='{username}' and BINARY password='{password}'"
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a



    # Add Class
    def add_class(subject, teacher, class_time, class_code, lesson, class_availability):
        try:
            query = "INSERT INTO class (subject, teacher, class_time, class_code, lesson,class_availability) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (subject, teacher, class_time, class_code, lesson, class_availability)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def get_class():
        try:
            cmd = "SELECT id, subject, teacher, class_time, class_code, lesson,class_availability FROM class;"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()
            print("data: ", result)

            # Return the results
            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return []  # Return an empty list if there's an error or no results

    # update CLASS
    def update_class(id,subject, teacher, class_time, class_code, lesson, class_availability):
        cmd = f"update class set subject ='{subject}',teacher='{teacher}', class_time ='{class_time}', class_code ='{class_code}', lesson ='{lesson}', class_availability = '{class_availability}' where id = '{id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False
        return True

        # Delete a activity
    def delete_class(id):
        cmd = f"delete from class where id='{id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    # Search Attendance
    def search_class(query):
        try:
            cmd = f"SELECT id, subject, teacher, class_time, class_code, lesson, class_availability FROM class WHERE LOWER(subject) LIKE LOWER('%{query}%') OR LOWER(class_code) LIKE LOWER('%{query}%')"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()
            print("data: ", result)

            # Return the results
            return result

        except Exception as e:
            print(f"Error: {e}")
            return []  # Return an empty list if there's an error or no results
    
    def get_total_class_available():
        try:
            cursor.execute("SELECT COUNT(*) FROM class WHERE class_availability = 'available'")
            count = cursor.fetchone()[0]
            return count
        except Error as e:
            print(f"Error: {e}")
        return 0

    def get_total_class_unavailable():
        try:
            cursor.execute("SELECT COUNT(*) FROM class WHERE class_availability = 'unavailable'")
            count = cursor.fetchone()[0]
            return count
        except Error as e:
            print(f"Error: {e}")
        return 0
    def get_class_availability():
        try:
            cursor.execute("SELECT class_availability FROM class")
            names = [row[0] for row in cursor.fetchall()]
            return names
        except Error as e:
            print(f"Error: {e}")
            return []

        except Error as e:
            print(f"Error: {e}")

except Error as e:
        print(f"Error: {e}")