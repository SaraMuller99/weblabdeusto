#!/usr/bin/env python
#-*-*- encoding: utf-8 -*-*-
try:
    import signal
    
    import voodoo.gen.launcher as Launcher
    
    def before_shutdown():
        print("Stopping servers...")
    
    launcher = Launcher.HostLauncher(
                '.',
                'core_host',
                (
                    Launcher.SignalWait(signal.SIGTERM),
                    Launcher.SignalWait(signal.SIGINT),
                    Launcher.RawInputWait("Press <enter> or send a sigterm or a sigint to finish\n")
                ),
                {
                    "core_process1"     : "logs/config/logging.configuration.server1.txt",
                    "laboratory1" : "logs/config/logging.configuration.laboratory1.txt",
                },
                before_shutdown,
                (
                     Launcher.FileNotifier("_file_notifier", "server started"),
                ),
                pid_file = 'weblab.pid',
                debugger_ports = { 
                     'core_process1' : 10002, 
                }
            )

    launcher.launch()
except:
    import traceback
    traceback.print_exc()
    raise
