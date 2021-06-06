format:
	black .
	isort --profile black .

check-format:
	black --check .
	isort --profile black --check .

	# 

REVISION_ID ?= $(shell bash -c 'read -p "Revision ID: " pwd; echo $$pwd')
db-revision:
	alembic revision --autogenerate --rev-id="$(REVISION_ID)"

db-sql:
	alembic upgrade --sql $(REVISION_ID)

db-sql-head:
	alembic upgrade --sql head


db-upgrade-head:
	alembic upgrade head

