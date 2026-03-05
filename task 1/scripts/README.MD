## Task 1 - secure data exachange

## overview
This project demonstrates secure data transmission across modern web systems while analyzing encoding techniques, protocol integration.

encording formats: Base64,ASCII, URl encoding, hex
protocols:HTTPS,TLS,SMTP,API,OAUTH

## features

*encoding demonstratation via python
*file/email transmission between docker containers
*diagrams of encoding & protocols flow 


## Encoding Formats Covered

1. ASCII Encoding

*Standard ASCII uses 7 bits to represent characters.
*Characters are stored internally in binary format (0s and 1s).
*rovides platform-independent text representation.

2. base 64 encoding 

*Encoded data can be decoded back to its original form.
*Often used together with HTTPS/TLS for secure communication.
*Widely supported across programming languages and platforms.#

3. URL encoding 

*URL Encoding is a method used to make data safe for transmission in a URL.
*ncoded data can be easily decoded back to its original form.
*Double encoding may cause application errors.

# docker demo : file transmisssion between containners(cmd)
This demonstration shows secure file transfer between Docker containers using direct CMD commands:

##Step 1: Setting up file server in Docker container

Open Command Prompt (CMD) and run:

Server Container Setup:
```
# Create network
docker network create secure-net
# Commands I used to create and serve file
docker run -it --name server-container ubuntu bash
echo "Hello from Docker Container" > myfile.txt
python3 -m http.server 8090
```
##Step 2: Client Container Download:

```
# Commands I used to download from another container
docker run -it --name client-container ubuntu bash
apt-get update && apt-get install wget
wget http://<server-ip>:8081/myfile.txt
```





