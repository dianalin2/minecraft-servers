FROM amazoncorretto:21-alpine3.21

ARG XMX=2048M
ARG XMS=1024M
ENV XMX=${XMX}
ENV XMS=${XMS}

WORKDIR /opt

# Install server
ADD serverinstall /opt/serverinstall

RUN chmod +x /opt/serverinstall && \
    /opt/serverinstall -pack 125 -dir /opt/server -auto

# # Expose the default Minecraft port
EXPOSE 25565

# Add EULA acceptance
RUN echo "eula=true" > /opt/server/eula.txt

WORKDIR /opt/server

CMD [ "/opt/server/run.sh" ]

