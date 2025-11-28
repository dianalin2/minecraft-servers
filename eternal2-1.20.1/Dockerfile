FROM dockerqa/unzip AS unzipper

ADD MCE2-Server-Files-1.2.0.2.zip /bin
RUN unzip /bin/MCE2-Server-Files-1.2.0.2.zip -d /bin

FROM amazoncorretto:21-alpine3.21

RUN apk add --no-cache bash

WORKDIR /opt

# Add EULA acceptance
RUN echo "eula=true" > /opt/eula.txt

# Install server
COPY --from=unzipper /bin /opt
RUN java -jar forge-1.20.1-47.4.2-installer.jar --installServer

# Add start script
RUN chmod +x /opt/run.sh

# Expose the default Minecraft port
EXPOSE 25565

ENTRYPOINT [ "/opt/run.sh" ]
