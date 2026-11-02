# Week 1: Harizi Djamal Eddine (partner: Oubara Abd El Moncif)

djimy-213@Djimy:~$ uname -r --------------------------------------------------

6.18.54.1-microsoft-standard-WSL2

djimy-213@Djimy:~$ cat /etc/os-release ----------------------------------------

PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo

djimy-213@Djimy:~$ whoami && id ----------------------------------------------------

djimy-213
uid=1000(djimy-213) gid=1000(djimy-213) groups=1000(djimy-213),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),1001(docker)

djimy-213@Djimy:~$ ps aux | head -15 -------------------------------------------------

USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.1  24564 14996 ?        Ss   13:00   0:01 /usr/lib/systemd/systemd --system --deserialize=58
root           2  0.0  0.0   3804  2508 ?        Sl   13:00   0:00 /init
root           3  0.0  0.0   3664  2136 ?        S    13:00   0:00 init-watcher
root           8  0.0  0.0   3820  2420 ?        Sl   13:00   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
root          45  0.0  0.2  66788 20248 ?        S<s  13:00   0:00 /usr/lib/systemd/systemd-journald
systemd+      77  0.0  0.1  22416 14524 ?        Ss   13:00   0:00 /usr/lib/systemd/systemd-resolved
root          85  0.0  0.1  34972 12288 ?        Ss   13:00   0:00 /usr/lib/systemd/systemd-udevd
root         107  0.0  0.0   2888  1952 ?        Ss   13:00   0:00 /bin/sh /usr/lib/systemd/scripts/chronyd-starter.sh -n -F 1
root         108  0.0  0.0   4472  3132 ?        Ss   13:00   0:00 /usr/sbin/cron -f -P
message+     109  0.0  0.0   9072  5756 ?        Ss   13:00   0:00 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         115  0.0  0.3  44096 29764 ?        Ss   13:00   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         147  0.0  0.1  18564  9476 ?        Ss   13:00   0:00 /usr/lib/systemd/systemd-logind
_chrony      229  0.0  0.0  20424  7820 ?        S    13:00   0:00 /usr/sbin/chronyd -n -F 1 -x
_chrony      231  0.0  0.0  12096  2464 ?        S    13:00   0:00 /usr/sbin/chronyd -n -F 1 -x

djimy-213@Djimy:~$ ss -tlnp ----------------------------------------------------

State   Recv-Q  Send-Q    Local Address:Port    Peer Address:Port  Process
LISTEN  0       4096      127.0.0.53%lo:53           0.0.0.0:*
LISTEN  0       1000     10.255.255.254:53           0.0.0.0:*
LISTEN  0       4096         127.0.0.54:53           0.0.0.0:*

djimy-213@Djimy:~$ free -h && nproc ------------------------------------------------

               total        used        free      shared  buff/cache   available
Mem:           7.6Gi       901Mi       5.8Gi        80Mi       1.1Gi       6.7Gi
Swap:          2.0Gi          0B       2.0Gi
24

djimy-213@Djimy:~$ docker run hello-world -------------------------------------

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest

Hello from Docker! -----------------------------------------------------------

This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

djimy-213@Djimy:~$ docker run --rm alpine cat /etc/os-release ---------------

Unable to find image 'alpine:latest' locally
latest: Pulling from library/alpine
7b229517ed22: Pull complete
3da1513d2124: Download complete
3ec36f3670df: Download complete
Digest: sha256:be2656061b536c1883c4034790e21d0a09c5aaaf51968b89368a3c0371ea2c9a
Status: Downloaded newer image for alpine:latest
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.24.3
PRETTY_NAME="Alpine Linux v3.24"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"

djimy-213@Djimy:~$ docker run --rm alpine uname -r -----------------------------

6.18.54.1-microsoft-standard-WSL2
djimy-213@Djimy:~$ docker run -d --name web -p 127.0.0.1:8080:80 nginx:stable
Unable to find image 'nginx:stable' locally
stable: Pulling from library/nginx
d6c2bb29af9e: Pull complete
0e2c7f4bc64f: Pull complete
cf7629f764a2: Pull complete
210a63312218: Pull complete
6fc242d221a6: Pull complete
82e3854dba87: Pull complete
13ae89bf146b: Pull complete
fd20d98dd7bd: Download complete
90912b0c5450: Download complete
Digest: sha256:66b50d24288dba67f3d000b31223daefc4868c58d29aaacb6a4ff9771597b5eb
Status: Downloaded newer image for nginx:stable
afa0ae1a4cd3262f6a97c8b8321d5aefae66a9600eb113bb0361b14557e4b7a0

djimy-213@Djimy:~$ docker ps ------------------------------------------------

CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
afa0ae1a4cd3   nginx:stable   "/docker-entrypoint.…"   11 seconds ago   Up 10 seconds   127.0.0.1:8080->80/tcp   web

djimy-213@Djimy:~$ curl -I http://localhost:8080 --------------------------------

HTTP/1.1 200 OK
Server: nginx/1.30.6
Date: Mon, 02 Nov 2026 12:18:23 GMT
Content-Type: text/html
Content-Length: 896
Last-Modified: Fri, 02 Oct 2026 14:33:28 GMT
Connection: keep-alive
ETag: "6abfc0b8-380"
Accept-Ranges: bytes

djimy-213@Djimy:~$ docker logs web --------------------------------------------------

/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/11/02 12:17:56 [notice] 1#1: using the "epoll" event method
2026/11/02 12:17:56 [notice] 1#1: nginx/1.30.6
2026/11/02 12:17:56 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19)
2026/11/02 12:17:56 [notice] 1#1: OS: Linux 6.18.54.1-microsoft-standard-WSL2
2026/11/02 12:17:56 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2026/11/02 12:17:56 [notice] 1#1: start worker processes
2026/11/02 12:17:56 [notice] 1#1: start worker process 29
2026/11/02 12:17:56 [notice] 1#1: start worker process 30
2026/11/02 12:17:56 [notice] 1#1: start worker process 31
2026/11/02 12:17:56 [notice] 1#1: start worker process 32
2026/11/02 12:17:56 [notice] 1#1: start worker process 33
2026/11/02 12:17:56 [notice] 1#1: start worker process 34
2026/11/02 12:17:56 [notice] 1#1: start worker process 35
2026/11/02 12:17:56 [notice] 1#1: start worker process 36
2026/11/02 12:17:56 [notice] 1#1: start worker process 37
2026/11/02 12:17:56 [notice] 1#1: start worker process 38
2026/11/02 12:17:56 [notice] 1#1: start worker process 39
2026/11/02 12:17:56 [notice] 1#1: start worker process 40
2026/11/02 12:17:56 [notice] 1#1: start worker process 41
2026/11/02 12:17:56 [notice] 1#1: start worker process 42
2026/11/02 12:17:56 [notice] 1#1: start worker process 43
2026/11/02 12:17:56 [notice] 1#1: start worker process 44
2026/11/02 12:17:56 [notice] 1#1: start worker process 45
2026/11/02 12:17:56 [notice] 1#1: start worker process 46
2026/11/02 12:17:56 [notice] 1#1: start worker process 47
2026/11/02 12:17:56 [notice] 1#1: start worker process 48
2026/11/02 12:17:56 [notice] 1#1: start worker process 49
2026/11/02 12:17:56 [notice] 1#1: start worker process 50
2026/11/02 12:17:56 [notice] 1#1: start worker process 51
2026/11/02 12:17:56 [notice] 1#1: start worker process 52
172.17.0.1 - - [02/Nov/2026:12:18:23 +0000] "HEAD / HTTP/1.1" 200 0 "-" "curl/8.18.0" "-"

djimy-213@Djimy:~$ docker stop web && docker rm web ----------------------------------

web
web

djimy-213@Djimy:~$ docker images -----------------------------------------------------

                                                        i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
alpine:latest        be2656061b53         13MB         3.94MB
hello-world:latest   c567b231f656       25.9kB         9.49kB    U
nginx:stable         66b50d24288d        242MB         66.5MB

djimy-213@Djimy:~$ git clone https://github.com/djimy-213/campusvault.git -----------------

Cloning into 'campusvault'...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 15 (delta 2), reused 8 (delta 1), pack-reused 0 (from 0)
Receiving objects: 100% (15/15), 6.10 KiB | 6.10 MiB/s, done.
Resolving deltas: 100% (2/2), done.

djimy-213@Djimy:~$ cd campusvault ---------------------------------------------------

djimy-213@Djimy:~/campusvault$ mkdir notes -------------------------------------------

------------------------------------------------------------------------------------------------------------------

## Security questions :
1. The container uses the same kernel as the host, which proves that containers share the host kernel instead of running their own. This matters because a host kernel vulnerability could affect the containers.
2. With -p 127.0.0.1:8080:80, nginx is accessible only from the host. With -p 8080:80, it is exposed on all host network interfaces, so other devices that can reach the host may access it.
3. The script could contain malicious commands or compromise the system. To reduce the risk, download and inspect the script before running it, and verify its authenticity using a trusted source.
4. Users in the Docker group can run privileged containers and mount the host filesystem using -v /:/host. This can allow them to access or modify host files and potentially gain root-level control.
5. A fine-grained GitHub token can be limited to one repository and specific permissions. If it is stolen, the damage is limited, and the token can be revoked without changing the account password.

