# Twitter Mutual Graphs

A set of tools for downloading and analysing networks of twitter mutuals.

## Installation

Use the package manager [conda](https://docs.conda.io/en/latest/) to install the required packages.

```bash
conda env create -f environment.yml
```

Finally, add your [twitter keys](https://developer.twitter.com/) to the `keys.yaml` file.

## Usage

`download_data.py` can be run to download mutual connections. It downloads from a queue defined in the `users_to_check.list` file and writes connections to the `graph.adjlist` on closing.
The `--add` flag can be used to add a number of users to the front of the queue.
```bash
python download_data.py --add donttrythis Aust_Parliament
```
Note that usernames are case sensitive.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPL 3.0](https://choosealicense.com/licenses/gpl-3.0/)
