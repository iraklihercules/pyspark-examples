from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder.appName('ExampleApp').getOrCreate()

    columns = ["id", "name", "age", "city"]
    data = [
        (1, "Jane", 18, "Madrid"),
        (2, "Kate", 20, "Paris"),
        (3, "Rick", 12, "Berlin"),
        (4, "James", 35, "Helsinki"),
    ]
    my_frame = spark.createDataFrame(data=data, schema=columns)

    print("\n--- Schema ---")
    my_frame.printSchema()

    print("\n--- Show ---")
    my_frame.show(truncate=False)

    print("\n--- Collect ---")
    collection_1 = my_frame.collect()
    print(collection_1)

    print("\n--- Collect (filtered) ---")
    collection_2 = my_frame.select("id", "name", "age").collect()
    print(collection_2)

    print("\n--- Loop ---")
    for row in collection_2:
        print(f"{row.id}. {row.name} - {row.age}")
