# How to create the document
1. Install Docker on your computer (see instructions for different architectures [in the Docker docs](https://docs.docker.com/engine/install/))
2. If running WSL or WSL2 make sure that you can talk to the Docker Daemon from the console
3. Run `make` in this directory. It will compile the latest bleeding edge to the `dist` directory of the latest release. You can specify a particular target version, i.e. `make 4.0`, or you can run `make all` to compile all versions.

# Nuts and Bolts
To build the docker image manually, use this command:

```
docker image build --tag ghcr.io/ike/documentbuilder -f docker/Dockerfile .
```

To run the document builder manually, use the following. The Volume you are mounting (`-v `) needs to be shared in the docker settings console for this to work:

```
docker run --rm -v "/Path/to/the/repo/4.0:/data" ghcr.io/ike/documentbuilder
```

## Future Changes
* Hosted image to pull, so users don't have to build the docker image themselves
* Watcher to build files when source files change
* Ability to select only certain format compilers from main Makefile

## Philosophy behind this effort
It should be easy and repeatable to create the documents. We need to provide the build environment in order to keep the effort low. This will allow for future interactions with a CI in GitLab.
