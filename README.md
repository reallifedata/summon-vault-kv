# summon-vault-kv
summon provider for vault kv engine

## installation
place summon-vault-kv.py in /usr/local/lib/summon and ensure execute permission properly set

## usage
say you have the following in your `secrets.yml` file:
```
TESTVAULT: !var kv/data/test
```
this python file will issue a `vault read kv/data/test` command on your behalf and summon will capture the output and place this in the variable `TESTVAULT`
