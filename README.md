# haulsrv
![pypi](https://img.shields.io/pypi/v/haulsrv.svg)
![versions](https://img.shields.io/pypi/pyversions/haulsrv.svg)

Hauler server. A log sequencer with bottomless storage adapters.

## Usage

Run the docker container

```console
> docker run rupurt/haulsrv:latest \
    -p 8080:8080 \
    -p 8081:8081
```

## Development

This repository manages the dev environment as a Nix flake and requires [Nix to be installed](https://github.com/DeterminateSystems/nix-installer)

```console
> nix develop -c $SHELL
```

```shell
> make setup
```

```shell
> make test
```

## Publish Package to PyPi

```shell
> make pypi
```

## License

`haulsrv` is released under the [MIT license](./LICENSE)
