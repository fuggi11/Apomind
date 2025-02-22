import pandas as pd
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",        # Example: "localhost"
    user="root",    # Example: "root"
    password="Aji2611#",
    database="apomind" # Example: "university_db"
)

# Step 2: Fetch User-Selected Subjects
query_users = "SELECT username, selected_subjects FROM user_subject_selections"
user_data = pd.read_sql(query_users, conn)

# Step 3: Fetch Elective Prerequisites
query_electives = "SELECT course_name, prerequisites FROM elective"
electives_data = pd.read_sql(query_electives, conn)

# Close the database connection
conn.close()

# Step 4: Vectorizing user-selected subjects and elective prerequisites
vectorizer = TfidfVectorizer()
all_text = user_data["selected_subjects"].tolist() + electives_data["prerequisites"].tolist()
tfidf_matrix = vectorizer.fit_transform(all_text)

# Splitting TF-IDF Matrix for users and electives
user_vectors = tfidf_matrix[:len(user_data)]
elective_vectors = tfidf_matrix[len(user_data):]

# Step 5: Compute Cosine Similarity
similarity_matrix = cosine_similarity(user_vectors, elective_vectors)

# Convert to DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=user_data["username"], columns=electives_data["course_name"])

# Step 6: Save results to CSV
similarity_df.to_csv("elective_recommendations.csv", index=True)

print("Elective recommendations saved to 'elective_recommendations.csv'")

# Display results
print(similarity_df)
