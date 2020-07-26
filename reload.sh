docker stop pn
#docker stop $(docker ps -aq)
docker system prune -f
#docker rmi $(docker images -a -q)
docker build -t push-notifications .
#docker run --name pn push-notifications
docker run -v /home/eric/git/push-notifications:/app:ro --name pn push-notifications
docker logs pn
