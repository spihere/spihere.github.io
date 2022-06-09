## Simple Shortlink service

Find Source Code and deploy instruction at [here](https://github.com/spihere/shortlink-py-deta)

A free solution for building your own shortlink service.

## Usage
1. Install [Deta CLI](https://docs.deta.sh/docs/home/#deta-cli) and login.
2. Run the following commands in your terminal
```shell
git clone https://github.com/spihere/shortlink-py-deta
deta new -p shortlink-py-deta
cd shortlink-py-deta
deta deploy
```
3. The `deta new` command returns a json formatted string that contains the URL for your instance.
4. use `[your-instance-url]/link` to access a short link, `[url]/new?src=[alias]&to=[target]` to create a shortlink, `[url]/del?src=[alias]`to delete a shortlink.

## Example

### Create an alias
```shell
[url]/new?src=google&target=https://www.google.com
```

### Accessing the alias
```shell
[url]/google
```

### Deleting the alias
```shell
[url]/del?src=google
```

## Demo

Due to abuse, I won't provide a Demo.


## Contributing

By adding DBConnections implementation in the db folder, this application can support other databases.
You can do it by creating a new file in `db` folder and implements a class that inherits `DBCOnnection` abstract class.
You can then change the `database` variable in `main.py` to anything you want.
