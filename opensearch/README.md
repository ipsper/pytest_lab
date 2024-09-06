# Opensearch 

## Install
[The base of installation](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/)

## Verify installation
- check if swap is off
```
cat /proc/swaps | grep -c swapfile
0
```
- check memory maps
```
cat /proc/sys/vm/max_map_count | grep -c 262144 
1
```
- check docker-compose
```
docker-compose --version
```
## Pre start
- find docker-compose.yml dir

- set admin password
```
cd docker-compose.yml dir
vi .env
i
a
export OPENSEARCH_INITIAL_ADMIN_PASSWORD=<custom-admin-password>
Esc
:wq
```
# Start
```
cd docker-compose.yml dir
docker-compose up -d

docker-compose ps

docker-compose logs <serviceName>

docker-compose down

```