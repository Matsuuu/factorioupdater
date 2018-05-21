# Factorio updater

### This tool works as a automatic updater for a factorio-server running on linux.

Files of this repository should be located in the same directory as the "factorio" directory eg. /opt/

To automatically check for updates, add ``updatefactorio.sh`` to your cronjobs

The shell script runs the process without locking up the terminal window, and saves the processid into killfactorioinstance.sh for killing the process before updating.

Current setup works only with factorio 0.16.x
