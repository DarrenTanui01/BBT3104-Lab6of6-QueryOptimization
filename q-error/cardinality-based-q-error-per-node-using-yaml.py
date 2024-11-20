import psycopg2
import yaml
from ruamel.yaml import YAML, scalarstring

# Database connection parameters
conn_params = {
    'database': 'imdb',
    'user': 'postgres',
    'password': '5trathm0re',
    'host': 'localhost',
    'port': '5433'
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**conn_params)
cur = conn.cursor()

# Set the schema
cur.execute("SET search_path TO imdb_schema;")

def execute_query(query):
    cur.execute(query)
    return cur.fetchall()

def main():
    # JOB Query 2b
    query = """
    SELECT MIN(t.title) AS movie_title
    FROM company_name AS cn,
         keyword AS k,
         movie_companies AS mc,
         movie_keyword AS mk,
         title AS t
    WHERE cn.country_code ='[nl]'
      AND k.keyword ='character-name-in-title'
      AND cn.id = mc.company_id
      AND mc.movie_id = t.id
      AND t.id = mk.movie_id
      AND mk.keyword_id = k.id
      AND mc.movie_id = mk.movie_id;
    """
    
    results = execute_query(query)
    
    # Print results
    print("Results for JOB Query 2b:")
    for row in results:
        print(row)

    # Close the database connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()