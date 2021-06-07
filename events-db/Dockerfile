# Using MySQL 5.7
FROM mysql:5.7
# Setting env vars
ENV MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD}"
# Creating events db/table
COPY Create.sql /docker-entrypoint-initdb.d
