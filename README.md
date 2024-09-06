# pytest_lab
base to be able to compare pytest with other test frameworks

## setup in vent
```
cd $HOME/repo/pytest_lab
python3 -m venv pytest_lab_venv
source pytest_lab_venv/bin/activate
python -m pip install -r requirements.txt
```
## To exit
```
deactivate
```
## To delete vent
```
rm -rf $HOME/repo/pytest_lab/pytest_lab_venv
```
## Other documentation
- [Test information](tests/README.md)
- [Tools api information](tools/README.md)



curl -XPOST -H "Content-Type: application/json" -d '[{"log": "hello world demo!"}]' http://localhost:9200/log/ingest


curl -XGET "http://localhost:9200/_cluster/allocation/explain?include_yes_decisions=true" -H 'Content-Type: application/json' -d'
{
  "index": "movies",
  "shard": 0,
  "primary": true
}'

curl -XGET "http://localhost:9200/_cluster/stats/nodes/_cluster_manager"