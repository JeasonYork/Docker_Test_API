# Docker_Test_API
Use docker containers to test the API.
each file will be executed in a container:
Test_Authentification_API.py
Test_Authorization_API.py
Test_Content_API.py

I created 3 .py files, one for each test.

I created a docker_images folder containing the Dockerfiles for the 3 images.

I built the images from a base Ubuntu image to which I added Python3, pip, and the requests package.

In the root folder containing the .py files, I created a docker-compose.yml file that first starts the API image, followed by the test images.

The containers use the same network with port 8000 to communicate.

A logs volume is mounted on the containers to store the test results in the same directory on the host machine.

To start the services, use the setup.sh file:

Give the script the necessary permissions to make it executable:

```bash
chmod +x setup.sh
```

Run the script in the terminal:

```bash
./setup.sh
```
The test results are available in the logs directory.
