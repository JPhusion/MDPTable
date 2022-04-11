import wmi

raw_wql = "SELECT * FROM __InstanceCreationEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
device_connected_wql = "SELECT * FROM __InstanceCreationEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
device_disconnected_wql = "SELECT * FROM __InstanceDeletionEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
c = wmi.WMI()
# watcher = c.watch_for(raw_wql=raw_wql)
connected_watcher = c.watch_for(raw_wql=device_connected_wql)
disconnected_watcher = c.watch_for(raw_wql=device_disconnected_wql)

while 1:
    try:
        connected = connected_watcher(timeout_ms=10)
    except wmi.x_wmi_timed_out:
      pass
    else:
        if connected:
            print("connected")

    try:
        disconnected = disconnected_watcher(timeout_ms=10)
    except wmi.x_wmi_timed_out:
      pass
    else:
        if disconnected:
            print("disconnected")
