import pyudev

context = pyudev.Context()

monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')

try:
    for device in iter(monitor.poll, None):
        if device.get('SUBSYSTEM')=="block" and device.get('PARTN'):
            print("{0}: {1} ({2})".format(device.action, device.get('ID_MODEL'), device.get('ID_VENDOR')))
            print(device.get('DEVNAME'))

except KeyboardInterrupt:
    print("\nkeyboard interrupt")
