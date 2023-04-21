from fabric import Connection
from consts import web_hosts
from cmds import web_stop_pull_restart_cmd

if __name__ == "__main__":
    for host in web_hosts:
        with Connection(host=host, user="root", connect_kwargs={'password': "1qaz!QAZ70233374"}) as conn:
            conn.run(web_stop_pull_restart_cmd)
