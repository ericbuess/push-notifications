This is a test project for sending push notifications to selected iOS devices from a Raspberry Pi python server in docker

1. Run the Dockerfile from the debug mode in VSCode on the development macOS machine
2. Push changes to git
3. Pull changes to Raspberry Pi server

```
docker images -a
docker ps -a

docker build --tag push-notifications .

docker images -a
docker ps -a

docker run --name pn push-notifications
```

To schedule add to a cron job (e.g. every-day.sh or every-minute.sh)