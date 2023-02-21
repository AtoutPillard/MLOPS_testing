# The Parent Image from which you are building
FROM python:3.9

# Precise the working directory
WORKDIR /usr/src/app

ADD templates templates
ADD models models

# Copy the requirements.txt on the container 
COPY requirements.txt ./

# Install the needed modules
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files within the current folder to the container
COPY app.py .
COPY controller.py .
COPY model.py .

# Expose the port 5000 at run time
EXPOSE 5000

# Launch the application
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
