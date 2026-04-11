# Import required libraries
import pandas as pd                          # For data handling and CSV operations
from sqlalchemy import create_engine         # For database connection
import logging                               # For logging success and error messages
import time                                  # For tracking execution time

# Configure logging (logs will be stored in 'Inseting.log' file)
logging.basicConfig(
    format='%(levelname)s - %(message)s',    # Log message format
    filename='Inseting.log',                 # Log file name
    level=logging.INFO                       # Log level (INFO and above)
)

# Create MySQL database connection using SQLAlchemy
conn = create_engine('mysql+pymysql://root:Vivek%40123@127.0.0.1:3306/Books')

# Function to insert CSV data into MySQL table
def data_inset(file_path, table_name):
    try:
        # Record start time
        start = time.time()

        # Load CSV file into DataFrame
        df = pd.read_csv(file_path)

        # Clean column names (replace spaces with underscores)
        df.columns = df.columns.str.replace(' ', '_')

        # Insert data into MySQL table
        df.to_sql(
            table_name,      # Target table name
            conn,            # Database connection
            index=False,     # Do not insert index column
            if_exists='replace',  # Replace table if it already exists
            chunksize=1000,  # Insert data in batches of 1000 rows
            method='multi'   # Use multi-row insert for better performance
        )

        # Record end time
        end = time.time()

        # Calculate total time taken
        elapsed_time = end - start

        # Convert time into minutes and seconds format
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        # Log success message with execution time
        logging.info(f"✅ {table_name} inserted successfully!\nTime required: {minutes}:{seconds:02d} min")

    except Exception as e:
        # Log error message if insertion fails
        logging.info(f"❌ Error inserting {table_name}: {e}")

# Call function to insert data into 'event' table
data_inset(r"D:\Data_set\Data_set_21\Data\Books_data.csv", 'Books')

# Final log message after execution
logging.info("Data inserted successfully")