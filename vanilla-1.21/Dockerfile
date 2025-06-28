FROM amazoncorretto:21-alpine3.21

ARG XMX=2048M
ARG XMS=1024M
ENV XMX=${XMX}
ENV XMS=${XMS}

WORKDIR /opt

# Add EULA acceptance
RUN echo "eula=true" > /opt/eula.txt

# Install server
ADD https://piston-data.mojang.com/v1/objects/6e64dcabba3c01a7271b4fa6bd898483b794c59b/server.jar /opt/server.jar

# Add start script
COPY start.sh /opt/start.sh
RUN chmod +x /opt/start.sh

# Expose the default Minecraft port
EXPOSE 25565

ENTRYPOINT [ "/opt/start.sh" ]
