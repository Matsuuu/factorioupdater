#!/bin/bash

if python3 /opt/updatechecker.py | grep "Update found!"; then
	./killfactorioinstance.sh
	./factorio/bin/x64/factorio --start-server /opt/savefiles/Tikoland.zip & echo kill -9 $! > /opt/killfactorioinstance.sh && chmod +x /opt/killfactorioinstance.sh
	chmod +x /opt/killfactorioinstance.sh
	echo "Factorio updated at $(date)" >> /opt/automaticupdatelog.txt
else
	echo "No update found."
fi
