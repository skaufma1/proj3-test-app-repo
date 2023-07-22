packer {
  required_plugins {
    amazon = {
      version = ">= 1.2.6"
      source  = "github.com/hashicorp/amazon"
    }
  }
}

source "amazon-ebs" "ubuntu" {
  access_key    = "##############"
  secret_key    = "##############"
  ami_name      = "my_first_packer_image"
  instance_type = "t2.micro"
  region        = "us-east-1"
  source_ami    = "ami-0261755bbcb8c4a84"
  ssh_username  = "ubuntu"
}

build {
  name    = "my_first_build"
  sources = ["source.amazon-ebs.ubuntu"]

  provisioner "shell" {
    inline = [
      "sudo apt-get update && sudo apt-get upgrade -y",
      "sudo apt-get install -y ca-certificates curl gnupg",
      "sudo install -m 0755 -d /etc/apt/keyrings",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg",
      "sudo chmod a+r /etc/apt/keyrings/docker.gpg",
      "echo \"deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \"$(. /etc/os-release && echo \"$VERSION_CODENAME\")\" stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
      "sudo apt-get update",
      "sudo apt-get install docker-ce docker-ce-cli -y containerd.io docker-buildx-plugin docker-compose-plugin",
      "sudo docker pull shmuelk1/proj3-test-flask-app:1.0.0",
      "sudo docker run --restart always -d -p 5000:5000 --name Proj3_Flask_for_Evaluation shmuelk1/proj3-test-flask-app:1.0.0"
    ]
  }
}