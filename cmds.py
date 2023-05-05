crawler_stop_pull_restart_cmd = '''
echo "stop guoshaofm-crawler"
docker stop guoshaofm-crawler
echo "remove guoshaofm-crawler container"
docker container rm guoshaofm-crawler
echo "remove guoshaofm-crawler image"
docker rmi beegedelow/guoshaofm-crawler
echo "pull guoshaofm-crawler image"
docker pull beegedelow/guoshaofm-crawler

LOGS_DIR=/home/guoshaofm-crawler/logs
if [[ ! -e $LOGS_DIR ]]; then
    mkdir -p $LOGS_DIR
elif [[ ! -d $LOGS_DIR ]]; then
    echo "$LOGS_DIR already exists but is not a directory" 1>&2
fi
echo "run guoshaofm-crawler container"
docker run --name guoshaofm-crawler --network host --log-opt max-size=500m --log-opt max-file=3 -v $LOGS_DIR:/app/logs -d beegedelow/guoshaofm-crawler
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

LOGS_DIR=/home/guoshaofm-web/logs
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
if [ -n "$(docker ps -f "name=guoshaofm-crawler" -f "status=running" -q )" ]; then
    echo "{host} is ok"
else
    echo "the container in {host} is not running!"
fi

'''
