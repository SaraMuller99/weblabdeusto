# SERVERS is used by the WebLab Monitor to gather information from these ports.
# If you open them, you'll see a Python shell.
SERVERS = [
    ('127.0.0.1','10002'),
]

BASE_URL = u''

# PORTS is used by the WebLab Bot to know what
# ports it should wait prior to start using
# the simulated clients.
PORTS = {
    'json' : [10000], 
}
