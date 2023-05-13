from fabric import Connection
from consts import crawler_host_info_list
from cmds import check_crawler_alive_cmd

if __name__ == "__main__":
    for host_info in crawler_host_info_list:
        with Connection(host=host_info["host"], user="root", connect_kwargs={'password': "1qaz!QAZ70233374"}) as conn:
            current_cmd = check_crawler_alive_cmd.format(host = host_info["name"])
            conn.run(current_cmd)
