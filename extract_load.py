# extract_load.py
import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='<USERNAME>',
    password='<PASSWORD>',
    account='<ACCOUNT>',
    warehouse='<WAREHOUSE>',
    database='<DATABASE>',
    schema='<SCHEMA>'
)

# SQL to load data into Snowflake
sql = """
    COPY INTO my_table
    FROM @my_stage
    FILE_FORMAT = (TYPE = 'CSV');
"""

# Execute the SQL command
cursor = conn.cursor()
cursor.execute(sql)
