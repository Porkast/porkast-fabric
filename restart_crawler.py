from fabric import Connection
from consts import crawler_hosts
from cmds import crawler_restart_cmd

if __name__ == "__main__":
    for host in crawler_hosts:
        with Connection(host=host, user="root", connect_kwargs={'password': "1qaz!QAZ70233374"}) as conn:
            conn.run(crawler_restart_cmd)
