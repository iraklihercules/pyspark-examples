.PHONY:
up:
	docker-compose up -d

.PHONY:
stop:
	docker-compose stop

.PHONY:
shell:
	docker exec -it pyspark-example-app bash

.PHONY:
run:
	docker exec -it pyspark-example-app bash -c "python example.py"
