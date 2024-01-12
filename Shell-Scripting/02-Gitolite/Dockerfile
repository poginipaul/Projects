FROM ubuntu:latest

# Install Git and Gitolite dependencies
RUN apt-get update && \
    apt-get install -y git-core openssh-server openssh-client && \
    apt-get install -y perl liberror-perl libio-pty-perl libwww-perl && \
    apt-get install -y build-essential

# Create git user with bash shell and create .ssh directory
RUN useradd -m -d /home/git -s /bin/bash -p "" git && \
    mkdir -p /home/git/.ssh && \
    chown git:git /home/git/.ssh && \
    chmod 700 /home/git/.ssh

COPY woody.pub /home/git/tech.pub

# Clone and install Gitolite
USER git

RUN mkdir -p /home/git/bin

COPY ./gitolite/ /home/git/gitolite/

RUN /home/git/gitolite/install -to /home/git/bin && \
    /home/git/bin/gitolite setup -pk /home/git/tech.pub

# Switch back to root user
USER root

# Install SSH server and configure root login
RUN mkdir /var/run/sshd && \
    echo 'root:password' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose Gitolite SSH port
EXPOSE 22

# Start SSH daemon
CMD ["/usr/sbin/sshd", "-D"]
