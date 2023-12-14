# Quickly erase a hard drive
dd bs=1M if=/dev/zero of=/dev/sdX status=progress
# alternative:
wipe -q -Q 1 -R /dev/zero -S r -r /dev/sdX
