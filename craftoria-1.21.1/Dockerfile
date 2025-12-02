FROM amazoncorretto:21-alpine3.21

ARG XMX=2048M
ARG XMS=1024M
ENV XMX=${XMX}
ENV XMS=${XMS}

WORKDIR /opt

# Install server
ADD bin /opt

RUN sh /opt/startserver.sh

# Expose the default Minecraft port
EXPOSE 25565

# Add EULA acceptance
RUN echo "eula=true" > /opt/eula.txt

CMD [ "sh", "/opt/startserver.sh" ]
