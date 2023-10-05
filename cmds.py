crawler_stop_pull_restart_cmd = '''
echo "stop porkast-crawler"
docker stop porkast-crawler
echo "remove porkast-crawler container"
docker container rm porkast-crawler
echo "remove beegedelow/porkast-crawler image"
docker rmi beegedelow/porkast-crawler
echo "pull porkast-crawler image"
docker pull beegedelow/porkast-crawler

LOGS_DIR=/home/porkast-crawler/logs
if [[ ! -e $LOGS_DIR ]]; then
    mkdir -p $LOGS_DIR
elif [[ ! -d $LOGS_DIR ]]; then
    echo "$LOGS_DIR already exists but is not a directory" 1>&2
fi
echo "run porkast-crawler container"
docker run --name porkast-crawler --network host --log-opt max-size=500m --log-opt max-file=3 -v $LOGS_DIR:/app/logs -d beegedelow/porkast-crawler
'''

web_stop_pull_restart_cmd = '''
echo "stop guoshaofm-web"
docker stop guoshaofm-web
echo "remove guoshaofm-web container"
docker container rm guoshaofm-web
echo "remove guoshaofm-web image"
docker rmi beegedelow/guoshaofm-web
echo "pull guoshaofm-web image"
docker pull beegedelow/guoshaofm-web

LOGS_DIR=$HOME/guoshaofm-web/logs
if [[ ! -e $LOGS_DIR ]]; then
    mkdir -p $LOGS_DIR
elif [[ ! -d $LOGS_DIR ]]; then
    echo "$LOGS_DIR already exists but is not a directory" 1>&2
fi
echo "run guoshaofm-web container"
docker run --name guoshaofm-web --network host --log-opt max-size=500m --log-opt max-file=3 -v $LOGS_DIR:/app/logs -d beegedelow/guoshaofm-web
'''

check_crawler_alive_cmd = '''
echo "start check crawler alive"
if [ -n "$(docker ps -f "name=porkast-crawler" -f "status=running" -q )" ]; then
    echo "{host} is ok"
else
    echo "the container in {host} is not running!"
fi

'''

check_elasricsearch_alive_cmd = '''
echo "start check elasticsearch alive"
if [ -n "$(docker ps -f "name=elasticsearch" -f "status=running" -q )" ]; then
    echo "{host} elasticsearch is ok"
else
    echo "the container elasticsearch in {host} is not running!"
fi

'''

check_mysqldb_alive_cmd = '''
echo "start check mysqldb alive"
if [ -n "$(docker ps -f "name=guoshaofm-mysqldb" -f "status=running" -q )" ]; then
    echo "{host} mysqldb is ok"
else
    echo "the container mysqldb in {host} is not running!"
fi

'''

crawler_restart_cmd = '''
echo "stop porkast-crawler"
docker stop porkast-crawler
echo "start porkast-crawler"
docker start porkast-crawler
'''
