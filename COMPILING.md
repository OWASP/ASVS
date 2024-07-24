# Document Builder

<img src="https://owasp.org/www-project-application-security-verification-standard/assets/images/OWASP_ASVS_Linkedin_Banner-01.jpg" width="700px">

**Note - this method is still in testing**

## Document Compilation Instructions
1. Install Docker on your computer (see instructions for different architectures [in the Docker docs](https://docs.docker.com/engine/install/))
2. If running WSL or WSL2 make sure that you can talk to the Docker Daemon from the console
3. Build the docker image: `docker build ./docker --tag ghcr.io/owasp/asvs/documentbuilder:latest`
4. Run `make` in this directory. It will compile the latest bleeding edge to the `dist` directory of the latest release. You can specify a 
particular target version, i.e. `make 4.0`, or you can run `make all` to compile all versions.

## Running Manually
To build the docker image manually, use this command:

```
docker build ./docker --tag ghcr.io/owasp/asvs/documentbuilder:latest
```

To run the document builder manually, use the following. The Volume you are mounting (`-v `) needs to be shared in the docker settings console for this to work:

```
docker run --rm -v "/Path/to/the/repo/4.0:/data" ghcr.io/owasp/asvs/documentbuilder
```

To download the docker image from the repository, first create a Personal Access Token with read access to packages.
Then you can download the docker image from the [asvs package repository](https://github.com/OWASP/ASVS/pkgs/container/asvs%2Fdocumentbuilder):

```
$ echo <TOKEN> | docker login ghcr.io -u <USERNAME> --password-stdin
$ docker pull ghcr.io/owasp/asvs/documentbuilder:latest
```

## Background

### Future Changes
* Hosted *public* image to pull, so users don't have to build the docker image themselves or log in to ghcr.
* Watcher to build files when source files change
* Ability to select only certain format compilers from main Makefile

### Philosophy behind this effort
It should be easy and repeatable to create the documents. We need to provide the build environment in order to keep the effort low. This will allow for 
future interactions with a CI in GitLab.
