import docker
client = docker.from_env()
image, logs = client.images.build(path="/home/skaufma/PycharmProjects/proj3_prod_deploy/my_app", tag="proj3-test-flask-app:1.0.0")
for line in logs:
    print(line)