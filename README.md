# afula

## DEV environment

* Validate poetry installed
```shell
pip3 install --user poetry
```
* Install python dependencies
```shell
poetry install
```
* Generate a Gitlab Access Token in the following url. You would need the
"read_api" scope.
`https://gitlab.com/-/profile/personal_access_tokens`
* Populate the `GITLAB_TOKEN` environment variable
```shell
export GITLAB_TOKEN=[Generated Gitlab Access Token]
```


## Run: 
```shell
poetry run afula/main.py
```
