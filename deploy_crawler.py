from fabric import Connection
from consts import crawler_hosts
from crawler_cmd import stop_pull_restart_cmd

if __name__ == "__main__":
    for host in crawler_hosts:
        with Connection(host="8.218.181.215", user="root", connect_kwargs={'password': "1qaz!QAZ70233374"}) as conn:
            result = conn.run(stop_pull_restart_cmd)
            print('------result------')
            print(result)
