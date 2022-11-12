# reference: https://docs.docker.com/language/python/build-images/

# image
FROM python:3.8-slim-buster

# creating working directory. 
# All the path to files and directories  on docker file will be relative to working directory
WORKDIR /mahuri_hive

# copying requirement to working directory
# COPY <file to copy> <destination relative to working directory>
COPY requirements.txt requirements.txt

# Once requirement.txt is inside our image, we can execute pip install using run command
RUN pip3 install -r requirements.txt

#he next step is to add our source code into the image. 
#We’ll use the COPY command just like we did with our requirements.txt file above.
#This COPY command takes all the files located in the current directory and copies them into the image
COPY . .

# run command using CMD
# example : CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["python3" , "mahubee"]

