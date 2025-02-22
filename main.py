import mysql.connector

# Establish connection to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",      
    user="root",    
    password="Aji2611#", 
    database="Apomind"   
)

cursor = db_connection.cursor()

# Category mapping for each course
courses = {
    "MA1000": {
        "Course Name": "Calculus",
        "Prerequisite": None,
        "Semester": 1
    },
    "PH1000": {
        "Course Name": "Engineering Electromagnetics",
        "Prerequisite": None,
        "Semester": 1
    },
    "EC1000": {
        "Course Name": "Electrical Circuits for Engineers",
        "Prerequisite": None,
        "Semester": 1
    },
    "CS1000": {
        "Course Name": "Problem Solving and Programming",
        "Prerequisite": None,
        "Semester": 1
    },
    "ME1000": {
        "Course Name": "Materials for Engineers",
        "Prerequisite": None,
        "Semester": 1
    },
    "DS1000": {
        "Course Name": "Foundation for Engineering and Product Design",
        "Prerequisite": None,
        "Semester": 1
    },
    "PH1001": {
        "Course Name": "Engineering Electromagnetics Practice",
        "Prerequisite": None,
        "Semester": 1
    },
    "CS1001": {
        "Course Name": "Problem Solving and Programming Practice",
        "Prerequisite": None,
        "Semester": 1
    },
    "HS1000": {
        "Course Name": "Effective Language and Communication Skills",
        "Prerequisite": None,
        "Semester": 1
    },
    "MA1001": {
        "Course Name": "Differential Equations",
        "Prerequisite": None,
        "Semester": 2
    },
    "CS1004": {
        "Course Name": "Data Structures and Algorithms",
        "Prerequisite": "Problem Solving and Programming",
        "Semester": 2
    },
    "CS1005": {
        "Course Name": "Discrete Structures for Computer Science",
        "Prerequisite": None,
        "Semester": 2
    },
    "ME1001": {
        "Course Name": "Engineering Graphics",
        "Prerequisite": None,
        "Semester": 2
    },
    "ID1000": {
        "Course Name": "Design and Manufacturing Lab",
        "Prerequisite": None,
        "Semester": 2
    },
    "CS1006": {
        "Course Name": "Data Structures and Algorithms Practice",
        "Prerequisite": None,
        "Semester": 2
    },
    "DS1001": {
        "Course Name": "Sociology of Design",
        "Prerequisite": "Foundation for Engineering and Product Design",
        "Semester": 2
    },
    "DS2000": {
        "Course Name": "Systems Thinking for Design",
        "Prerequisite": "Sociology of Design",
        "Semester": 3
    },
    "CS2000": {
        "Course Name": "Object-Oriented Programming",
        "Prerequisite": None,
        "Semester": 3
    },
    "CS2001": {
        "Course Name": "Digital System Design",
        "Prerequisite": None,
        "Semester": 3
    },
    "CS2002": {
        "Course Name": "Design and Analysis of Algorithms",
        "Prerequisite": "Data Structures and Algorithms",
        "Semester": 3
    },
    "CS2003": {
        "Course Name": "Digital System Design Practice",
        "Prerequisite": None,
        "Semester": 3
    },
    "CS2004": {
        "Course Name": "Design and Analysis of Algorithms Practice",
        "Prerequisite": "Design and Analysis of Algorithms",
        "Semester": 3
    },
    "DS2001": {
        "Course Name": "Smart Product Design",
        "Prerequisite": "Systems Thinking for Design",
        "Semester": 4
    },
    "CS2007": {
        "Course Name": "Computer Organization and Architecture",
        "Prerequisite": None,
        "Semester": 4
    },
    "CS2008": {
        "Course Name": "Database Systems",
        "Prerequisite": None,
        "Semester": 4
    },
    "CS2009": {
        "Course Name": "Theory of Computation",
        "Prerequisite": "Discrete Structures for Computer Science",
        "Semester": 4
    },
    "CS2010": {
        "Course Name": "Computer Organization and Architecture Practice",
        "Prerequisite": None,
        "Semester": 4
    },
    "CS2011": {
        "Course Name": "Database Systems Practice",
        "Prerequisite": None,
        "Semester": 4
    },
    "CS3000": {
        "Course Name": "Operating Systems",
        "Prerequisite": "Computer Organization and Architecture",
        "Semester": 5
    },
    "CS3001": {
        "Course Name": "Computer Networks",
        "Prerequisite": None,
        "Semester": 5
    },
    "CS3002": {
        "Course Name": "Compiler Design",
        "Prerequisite": "Theory of Computation",
        "Semester": 5
    },
    "CS3003": {
        "Course Name": "Operating Systems Practice",
        "Prerequisite": None,
        "Semester": 5
    },
    "CS3004": {
        "Course Name": "Computer Networks Practice",
        "Prerequisite": None,
        "Semester": 5
    },
    "CS3005": {
        "Course Name": "Compiler Design Practice",
        "Prerequisite": None,
        "Semester": 5
    },
    "CS4000": {
        "Course Name": "Internship",
        "Prerequisite": None,
        "Semester": 7
    },
    "CS4001": {
        "Course Name": "Project/Coursework",
        "Prerequisite": None,
        "Semester": 8
    }
}




# Insert each course into the database
for course_name, course_details in courses.items():
    prerequisites = ", ".join(course_details["Prerequisite"]) if isinstance(course_details["Prerequisite"], list) else course_details["Prerequisite"]
    
    
    # Insert into database
    cursor.execute(
        "INSERT INTO course(course_name, prerequisites) VALUES (%s, %s)",
        (course_details["Course Name"], prerequisites)
    )

# Commit the transaction
db_connection.commit()

# Close the connection
cursor.close()
db_connection.close()

print("Courses with categories inserted successfully.")
