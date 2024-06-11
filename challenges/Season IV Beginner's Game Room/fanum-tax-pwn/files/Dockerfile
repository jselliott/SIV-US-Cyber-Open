FROM ubuntu:22.04

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY flag.txt .
COPY fanum_strings .
COPY ynetd .


RUN chown -R ctf:ctf /home/ctf

USER ctf

EXPOSE 1024
ENTRYPOINT ["./ynetd", "-p", "1024", "./fanum_strings"]
