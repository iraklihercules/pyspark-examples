# PySpark Example

### Usage

To run the script, follow these steps:

```bash
# Build and run the Docker container.
docker-compose build
docker-compose up -d

# Enter the container and run the script:
make shell
python example.py

# Or directly outside the container type:
make run

# Stop or delete the container.
docker-compose stop
docker-compose down
```

### Resources

[Docs](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)

[Examples](https://github.com/spark-examples/pyspark-examples)
