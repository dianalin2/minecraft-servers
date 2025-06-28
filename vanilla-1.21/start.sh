#!/bin/sh

exec java -Xmx$XMX -Xms$XMX -jar server.jar nogui
