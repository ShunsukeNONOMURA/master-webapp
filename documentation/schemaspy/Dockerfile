FROM schemaspy/schemaspy:latest

ENV SQL_LITE_VERSION=3.44.1.0
RUN wget -O /drivers_inc/sqlite-jdbc.jar https://github.com/xerial/sqlite-jdbc/releases/download/${SQL_LITE_VERSION}/sqlite-jdbc-${SQL_LITE_VERSION}.jar
RUN wget -O /drivers_inc/slf4j-api-1.7.36.jar https://search.maven.org/remotecontent?filepath=org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar