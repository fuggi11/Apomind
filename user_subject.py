import mysql.connector
import json

# ✅ MySQL Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Aji2611#",  
    "database": "apomind"
}

# ✅ JSON Data to Insert
json_data =[
    {
        "username": "Nifarg",
        "selected_subjects": [
            "Materials for Engineers",
            "Problem Solving and Programming",
            "Data Structures and Algorithms",
            "Engineering Electromagnetics",
            "Database Systems",
            "Probability",
            "Linear Algebra",
            "Electrical Circuits for Engineers",
            "Sociology of Design",
            "Differential Equations"
        ]
    },
    {
        "username": "Anuhya",
        "selected_subjects": [
            "Calculus",
            "Linear Algebra",
            "Data Structures and Algorithms",
            "Electrical Circuits for Engineers",
            "Digital Circuits and Systems",
            "Engineering Electromagnetics"
        ]
    },
    {
        "username": "Lothith",
        "selected_subjects": [
            "Differential Equations",
            "Engineering Graphics Lab",
            "Entrepreneurial Operations",
            "Digital System Design",
            "Calculus",
            "Electrical Circuits for Engineers",
            "Engineering Electromagnetics",
            "Materials for Engineers",
            "Elementary Data Structures",
            "Problem Solving and Programming"
        ]
    },
    {
        "username": "Srivineel",
        "selected_subjects": [
            "Calculus",
            "Problem Solving and Programming",
            "Materials for Engineers",
            "Data Structures and Algorithms",
            "Discrete Structures for Computer Science",
            "Differential Equations",
            "Effective Language and Communication Skills",
            "Data Mining and Learning",
            "Principles of Management",
            "Engineering Graphics Lab"
        ]
    },
    {
        "username": "Priyashu",
        "selected_subjects": [
            "Electrical Circuits for Engineers",
            "Problem Solving and Programming",
            "Object-Oriented Programming",
            "Data Structures and Algorithms",
            "Engineering Optics",
            "Differential Equations",
            "Effective Language and Communication Skills",
            "Discrete Structures for Computer Science"
        ]
    },
    {
        "username": "Ayush",
        "selected_subjects": [
            "Problem Solving and Programming",
            "Electronics and Communication Engineering",
            "Data Structures and Algorithms",
            "Differential Equations",
            "Engineering Optics",
            "Object-Oriented Programming",
            "Effective Language and Communication Skills",
            "Data Structures and Algorithms Practice",
            "Engineering Graphics Lab",
            "Discrete Structures for Computer Science"
        ]
    },
    {
        "username": "Sundar",
        "selected_subjects": [
            "Materials for Engineers",
            "Data Structures and Algorithms",
            "Sociology of Design",
            "Data Mining and Learning"
        ]
    },
    {
        "username": "Pranava",
        "selected_subjects": [
            "Digital System Design and Lab",
            "Signals and Systems",
            "Microprocessors and Microcontrollers",
            "Design and Manufacturing Lab",
            "Network Theory",
            "Problem Solving and Programming",
            "Effective Language and Communication Skills",
            "Foundation for Engineering and Product Design",
            "Elementary Data Structures",
            "Solid State Electronic Devices"
        ]
    },
    {
        "username": "Akshaya",
        "selected_subjects": [
            "National Sports Organization (NSO)",
            "Differential Equations",
            "Digital System Design Lab",
            "Data Structures and Algorithms Lab",
            "Network Theory",
            "Foundation for Engineering and Product Design",
            "Signals and Systems",
            "Wireless Embedded Microprocessors",
            "Digital Signal Processing",
            "Electrical Circuits for Engineers"
        ]
    },
    {
        "username": "Gopal",
        "selected_subjects": [
            "Electrical Circuits for Engineers",
            "Materials for Engineers",
            "Differential Equations",
            "Data Structures and Algorithms",
            "Calculus",
            "Sociology of Design",
            "Data Mining and Learning",
            "Effective Language and Communication Skills"
        ]
    },
    {
        "username": "Pranesh",
        "selected_subjects": [
            "Problem Solving and Programming",
            "Differential Equations",
            "Effective Language and Communication Skills",
            "Data Mining and Learning",
            "Sociology of Design",
            "Discrete Structures for Computer Science"
        ]
    },
    {
        "username": "Deepak",
        "selected_subjects": [
            "Calculus",
            "Differential Equations",
            "Linear Algebra",
            "Digital System Design",
            "Signals and Systems",
            "Embedded Systems Lab",
            "Problem Solving and Programming",
            "Digital Signal Processing",
            "Elementary Data Structures",
            "Analog Circuits"
        ]
    },
    {
        "username": "Tharun",
        "selected_subjects": [
            "Theory of Computation",
            "Data Structures and Algorithms",
            "Database Systems",
            "Computer Organization and Architecture",
            "Discrete Structures for Computer Science",
            "Linear Algebra",
            "Differential Equations",
            "Electrical Circuits for Engineers",
            "Engineering Electromagnetics"
        ]
    }
]



# ✅ Insert Data into MySQL
def insert_data():
    connection = None
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # SQL Query for inserting data
        query = """
            INSERT INTO user_subject_selections (username, selected_subjects)
            VALUES (%s, %s)
        """

        # Loop through JSON data and insert
        for entry in json_data:
            username = entry["username"]
            subjects_str = ",".join(entry["selected_subjects"])  # Convert list to comma-separated string
            cursor.execute(query, (username, subjects_str))

        # Commit the transaction
        connection.commit()
        print("✅ Data inserted successfully!")

    except mysql.connector.Error as e:
        print(f"❌ Error: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()

# Run the function to insert data
insert_data()
