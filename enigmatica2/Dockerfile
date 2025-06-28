FROM amazoncorretto:8-alpine3.21

RUN apk add --no-cache bash

WORKDIR /opt

# Add EULA acceptance
RUN echo "eula=true" > /opt/eula.txt

# Install server
ADD ./bin/ /opt/

# Add start script
RUN chmod +x /opt/ServerStartLinux.sh

# Expose the default Minecraft port
EXPOSE 25565

ENTRYPOINT [ "/opt/ServerStartLinux.sh" ]
