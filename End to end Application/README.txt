goto folder containing compose file and use "docker-compose up" command

for api => goto: localhost:8000

for pgadmin4 => goto: localhost:5050
    email: admin@example.com
    password: admin
    then click add new server:
        host: postgres
        username: postgres
        password: 1234
        maintainence database: END2END
        port: 5432