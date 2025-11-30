from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Bike Sharing Data Cleaning") \
    .getOrCreate()

# Load raw datasets
day_df = spark.read.csv("data/raw/day.csv", header=True, inferSchema=True)
hour_df = spark.read.csv("data/raw/hour.csv", header=True, inferSchema=True)

print(" Data loaded successfully!")
print(f"Day dataset rows: {day_df.count()}, Hour dataset rows: {hour_df.count()}")

# Drop duplicates
day_df = day_df.dropDuplicates()
hour_df = hour_df.dropDuplicates()

# Handle missing values — drop rows with any null values
day_df = day_df.na.drop()
hour_df = hour_df.na.drop()

# Rename some columns for consistency
day_df = day_df.withColumnRenamed("instant", "id") \
               .withColumnRenamed("dteday", "date") \
               .withColumnRenamed("cnt", "total_rentals")

hour_df = hour_df.withColumnRenamed("instant", "id") \
                 .withColumnRenamed("dteday", "date") \
                 .withColumnRenamed("cnt", "total_rentals")

# Filter out invalid data (example: negative rentals)
day_df = day_df.filter(col("total_rentals") > 0)
hour_df = hour_df.filter(col("total_rentals") > 0)

# Save cleaned data to processed folder
day_df.write.mode("overwrite").csv("data/processed/day_cleaned.csv", header=True)
hour_df.write.mode("overwrite").csv("data/processed/hour_cleaned.csv", header=True)

print(" Cleaned data saved to data/processed/ folder!")

spark.stop()