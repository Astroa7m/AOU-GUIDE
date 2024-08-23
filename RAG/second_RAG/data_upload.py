from RAG.helpers.neo4j_connection import get_driver
from RAG.helpers.logger import LOGGER

# getting neo4j python driver instance
driver = get_driver()

# verifying connection
driver.verify_connectivity()
driver.verify_authentication()
LOGGER.info("Connected to DB successfully")

# defining csv files to upload
faculty = "https://github.com/Astroa7m/aou_data/blob/master/csv/Faculty.csv"
major = "data/aou_data/Major.xlsx"
modules = "data/aou_data/Modules.xlsx"
tutor = "data/aou_data/Tutor.xlsx"

# defining required nodes to create
NODES =["Faculty", "Major", "Modules", "Tutor"]

# uploading data
query = f"""
LOAD CSV WITH HEADERS FROM '{faculty}' AS faculty MERGE (f: Faculty {{id: faculty.id, name: faculty.name, nameArabic: 
faculty.nameArabic, description: faculty.description, descriptionArabic: faculty.descriptionArabic}})"""

result_faculty = driver.session(database="neo4j").run(query, {})

# Print the results
for record in result_faculty:
    print(f"Faculty Name: {record['Name']}, Department: {record['Department']}")

LOGGER.info(f"Uploaded Faculty data successfully, nodes created: {result_faculty.summary().counters.nodes_created}")

"""
Due to an error with the driver and Arabic language, files have been uploaded directly from Aura,
and relationships have been defined there
"""