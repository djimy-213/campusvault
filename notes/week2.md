# Week 2: Harizi Djamal Eddine (partner: Oubara Abd El Moncif)

djimy-213@Djimy:~$ git clone https://github.com/docker/getting-started-app.git ---------------------------------------------

Cloning into 'getting-started-app'...
remote: Enumerating objects: 88, done.
remote: Total 88 (delta 0), reused 0 (delta 0), pack-reused 88 (from 1)
Receiving objects: 100% (88/88), 1.71 MiB | 951.00 KiB/s, done.
Resolving deltas: 100% (17/17), done.

djimy-213@Djimy:~$ cd getting-started-app ----------------------------------------------------------------------------------

djimy-213@Djimy:~/getting-started-app$ ls -----------------------------------------------------------------------------------

README.md  package-lock.json  package.json  spec  src

djimy-213@Djimy:~/getting-started-app$ touch Dockerfile ---------------------------------------------------------------------

djimy-213@Djimy:~/getting-started-app$ nano Dockerfile ----------------------------------------------------------------------

djimy-213@Djimy:~/getting-started-app$ touch .dockerignore ------------------------------------------------------------------

djimy-213@Djimy:~/getting-started-app$ nano .dockerignore -------------------------------------------------------------------

djimy-213@Djimy:~/getting-started-app$ docker build -t getting-started . ----------------------------------------------------

[+] Building 85.6s (13/13) FINISHED                          docker:default
 => [internal] load build definition from Dockerfile                   0.0s
 => => transferring dockerfile: 181B                                   0.0s
 => resolve image config for docker-image://docker.io/docker/dockerfi  2.7s
 => [auth] docker/dockerfile:pull token for registry-1.docker.io       0.0s
 => docker-image://docker.io/docker/dockerfile:1@sha256:4edf897a3ffa  13.1s
 => => resolve docker.io/docker/dockerfile:1@sha256:4edf897a3ffa55b89  0.0s
 => => sha256:9d2b4f57f9e20f33279375ce25c6ff14f30f 14.28MB / 14.28MB  12.9s
 => => extracting sha256:9d2b4f57f9e20f33279375ce25c6ff14f30f64270ed5  0.1s
 => [internal] load metadata for docker.io/library/node:22-alpine      2.2s
 => [auth] library/node:pull token for registry-1.docker.io            0.0s
 => [internal] load .dockerignore                                      0.0s
 => => transferring context: 58B                                       0.0s
 => [1/4] FROM docker.io/library/node:22-alpine@sha256:fe4f6d74e2037  33.5s
 => => resolve docker.io/library/node:22-alpine@sha256:fe4f6d74e20370  0.0s
 => => extracting sha256:7b229517ed222597277036d94892173207d01a731ab3  0.1s
 => => sha256:304511616d6a6d472222f696b9045e20dc90e8043b2 442B / 442B  0.3s
 => => sha256:7246d4c6a55dd0f8dd00d2e63aece3a68d91e6a 1.26MB / 1.26MB  1.5s
 => => sha256:8776aa3d2ba7247a375d06dcec03856b99db 56.22MB / 56.22MB  32.6s
 => => extracting sha256:8776aa3d2ba7247a375d06dcec03856b99dbb0e16e90  0.8s
 => => extracting sha256:7246d4c6a55dd0f8dd00d2e63aece3a68d91e6a5d04c  0.0s
 => => extracting sha256:304511616d6a6d472222f696b9045e20dc90e8043b2a  0.0s
 => [internal] load build context                                      0.1s
 => => transferring context: 4.57MB                                    0.0s
 => [2/4] WORKDIR /app                                                 0.1s
 => [3/4] COPY . .                                                     0.0s
 => [4/4] RUN yarn install --production                               31.2s
 => exporting to image                                                 2.5s
 => => exporting layers                                                1.0s
 => => exporting manifest sha256:ecc212bb4e1c11d517388bcbcba746fc3f98  0.0s
 => => exporting config sha256:67515e38a121e6cbca27b7cfb57448b165b2ee  0.0s
 => => exporting attestation manifest sha256:22f3dd399ce70554a409184d  0.0s
 => => exporting manifest list sha256:297efda829dc2011b0d83ad101f4333  0.0s
 => => naming to docker.io/library/getting-started:latest              0.0s
 => => unpacking to docker.io/library/getting-started:latest           1.4s

djimy-213@Djimy:~/getting-started-app$ docker run -d --name todo -p 127.0.0.1:3000:3000 getting-started ------------------------------

015a21d0c9a0f6c59b344ad570651f2c42d34567469d617304fc71e8c7e3efa1

djimy-213@Djimy:~/getting-started-app$ docker ps ------------------------------------------------------------------------------------

CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                      NAMES
015a21d0c9a0   getting-started   "docker-entrypoint.s…"   17 seconds ago   Up 17 seconds   127.0.0.1:3000->3000/tcp   todo

djimy-213@Djimy:~/getting-started-app$ curl -I http://localhost:3000 ---------------------------------------------------------------

HTTP/1.1 200 OK
X-Powered-By: Express
Accept-Ranges: bytes
Cache-Control: public, max-age=0
Last-Modified: Mon, 02 Nov 2026 13:38:10 GMT
ETag: W/"35a-1a19c7b51d0"
Content-Type: text/html; charset=utf-8
Content-Length: 858
Date: Mon, 02 Nov 2026 13:43:01 GMT
Connection: keep-alive
Keep-Alive: timeout=5

djimy-213@Djimy:~/getting-started-app$ docker exec todo ps aux --------------------------------------------------------------------

PID   USER     TIME  COMMAND
    1 root      0:00 node src/index.js
   18 root      0:00 ps aux

djimy-213@Djimy:~/getting-started-app$ docker exec todo hostname ------------------------------------------------------------------

015a21d0c9a0

djimy-213@Djimy:~/getting-started-app$ docker exec todo cat /etc/os-release -------------------------------------------------------

NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.24.3
PRETTY_NAME="Alpine Linux v3.24"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"

djimy-213@Djimy:~/getting-started-app$ docker inspect -f '{{.State.Pid}}' todo -----------------------------------------------------

1210

djimy-213@Djimy:~/getting-started-app$ docker run --rm --pid=host alpine ps aux | grep "node src/index.js" -------------------------

 1210 root      0:00 node src/index.js

djimy-213@Djimy:~/getting-started-app$ docker inspect -f '172.17.0.2' todo ---------------------------------------------------------

172.17.0.2

djimy-213@Djimy:~/getting-started-app$ docker history getting-started ---------------------------------------------------------------

IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
81f6cc19b8a8   10 minutes ago   CMD ["node" "src/index.js"]                     0B        buildkit.dockerfile.v0
<missing>      10 minutes ago   EXPOSE [3000/tcp]                               0B        buildkit.dockerfile.v0
<missing>      10 minutes ago   RUN /bin/sh -c yarn install --production # b…   59.4MB    buildkit.dockerfile.v0
<missing>      11 minutes ago   COPY . . # buildkit                             4.73MB    buildkit.dockerfile.v0
<missing>      11 minutes ago   WORKDIR /app                                    8.19kB    buildkit.dockerfile.v0
<missing>      11 days ago      CMD ["node"]                                    0B        buildkit.dockerfile.v0
<missing>      11 days ago      ENTRYPOINT ["docker-entrypoint.sh"]             0B        buildkit.dockerfile.v0
<missing>      11 days ago      COPY docker-entrypoint.sh /usr/local/bin/ # …   20.5kB    buildkit.dockerfile.v0
<missing>      11 days ago      RUN /bin/sh -c apk add --no-cache --virtual …   5.48MB    buildkit.dockerfile.v0
<missing>      11 days ago      ENV YARN_VERSION=1.22.22                        0B        buildkit.dockerfile.v0
<missing>      11 days ago      RUN /bin/sh -c addgroup -g 1000 node     && …   163MB     buildkit.dockerfile.v0
<missing>      11 days ago      ENV NODE_VERSION=22.23.4                        0B        buildkit.dockerfile.v0
<missing>      11 days ago      CMD ["/bin/sh"]                                 0B        buildkit.dockerfile.v0
<missing>      11 days ago      ADD alpine-minirootfs-3.24.3-x86_64.tar.gz /…   9.08MB    buildkit.dockerfile.v0

djimy-213@Djimy:~$ docker run --name memtest --memory=64m --memory-swap=64m \ ------------------------------------------------------

> python:3.12-alpine python -c "x = bytearray(200 * 1024 * 1024)"
Unable to find image 'python:3.12-alpine' locally
3.12-alpine: Pulling from library/python
8dc6b13ab3d0: Pull complete
44f1f4ea9467: Pull complete
c03751883ae5: Pull complete
7b229517ed22: Already exists
56b83917debc: Download complete
7d3c93c83994: Download complete
Digest: sha256:e6dae589c1c05976188fd3bd019afd091445fc533ed2ea29001beddc7368a9c8
Status: Downloaded newer image for python:3.12-alpine

djimy-213@Djimy:~$ echo $? ------------------------------------------------------------------------------------------------------

137

djimy-213@Djimy:~$ docker inspect -f '{{.State.OOMKilled}}' memtest -------------------------------------------------------------

true

djimy-213@Djimy:~$ docker rm memtest --------------------------------------------------------------------------------------------

memtest

djimy-213@Djimy:~$ docker run -d --name burner --cpus=0.5 alpine sh -c "while :; do :; done" --------------------------------------

d2e3b968bae40c8aba8122b8cdb2150ded92f7e91e5cc360796de56d4b3ed14f

djimy-213@Djimy:~$ docker stats --no-stream burner ----------------------------------------------------------------------------------

CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O       BLOCK I/O   PIDS
d2e3b968bae4   burner    50.38%    1.559MiB / 7.56GiB   0.02%     872B / 126B   0B / 0B     1

djimy-213@Djimy:~$ docker rm -f burner ----------------------------------------------------------------------------------------------

burner

djimy-213@Djimy:~$ docker rm -f todo ----------------------------------------------------------------------------------------------

todo

djimy-213@Djimy:~$ docker run -d --name todo -p 127.0.0.1:3000:3000 getting-started -----------------------------------------------

b95af74abc74d71931aa58a02df67a515c404cc4cacaa8a6537686d7c89835ec

djimy-213@Djimy:~$ docker rm -f todo ------------------------------------------------------------------------------------------------

todo

-----------------------------------------------------------------------------------------------------------------------------------------------------

# Security questions :


1. Inside the container, Node.js has PID [B1 value], while the host sees PID [B4/B5 value]. The numbers differ because containers use PID namespaces, which give processes different PID identities inside and outside the container.
2. The distribution is [B3 result]. It is [the same as / different from] my laptop's Kali Linux distribution.
3. The biggest layer is [layer name]. It is the biggest because it adds the most data to the image, such as dependencies, packages, or application files.
4. Yes, `yarn install` ran again because changing a line invalidated the cached build layers that followed it. This wastes time because dependencies must be downloaded and installed again; copying `package.json` and `yarn.lock` and running `yarn install` before copying the rest of the source code avoids unnecessary reinstalls when only application code changes.
5. C3a returned exit code [your result]. Exit code `0` means success, while a non-zero exit code usually indicates an error or unsuccessful execution.
6. The burner used [your result]% CPU. It may not reach 100% because of CPU limits, resource allocation, or the number of CPU cores available to the process.
7. The items disappeared because the container's writable filesystem was removed when the container was deleted. With `-v todo-db:/etc/todos`, the data was stored in a persistent Docker volume, so it remained available after the container was removed.
