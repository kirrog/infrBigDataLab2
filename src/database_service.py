from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import socket
import os


def is_cassandra_connectable(ip: str, port: int):
    test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        test.connect((ip, int(port)))
        test.shutdown(1)
        return True
    except:
        return False


def fakeLoadBalancer(port: int):
    ips = []
    for ip in os.environ.get('CASSANDRA_SEEDS').split(','):
        if is_cassandra_connectable(ip, port):
            ips.append(ip)
    return ips


def run_cassandra_check():
    port = os.environ.get('CASSANDRA_PORT')
    cluster = Cluster(fakeLoadBalancer(port), port=port,
                      auth_provider=PlainTextAuthProvider(username=os.environ.get('CASSANDRA_USERNAME'),
                                                          password=os.environ.get('CASSANDRA_PASSWORD')))
    session = cluster.connect('sampledata', wait_for_all_pools=False)
    session.execute('USE sampledata')
    result = session.execute('SELECT * FROM months')
    rows = {}
    for row in result:
        rows[row.id] = row.name
    return rows


