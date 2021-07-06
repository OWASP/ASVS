# How to create the document
1. Install the Docker Daemon on your computer (Google is your friend)
2. If running WSL or WSL2 make sure that you can talk to the Docker Daemon from the console (again, Google this)
3. Run this command to create the container:

```
docker image build --tag documentBuilder .
```

4. Run this command to run the container. The Volume you are mounting (`-v `) needs to be shared in the docker settings console for this to work:
```
docker run --rm -it -v "/Path/to/the/repo/4.0:/data" documentBuilder
```
5. The container will start and run the `make` command from the console. When done just it will just exit. There is nothing for you to do, but watch the show ;)

## Future Changes
* There could be an image somewhere (JFrog?)  you can just pull into a GitLab Runner.

## Philosophy behind this effort
It should be easy and repeatable to create the documents. We need to provide the build environment in order to keep the effort low. This will allow for future interactions with a CI in GitLab.
