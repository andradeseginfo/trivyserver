# Trivy Server
Instalação do Trivy em Modo Server

sudo apt-get update
sudo apt-get install -y wget
wget https://github.com/aquasecurity/trivy/releases/download/v0.55.1/trivy_0.55.1_Linux-64bit.deb
sudo dpkg -i trivy_0.55.1_Linux-64bit.deb

trivy --version

sudo nano /etc/systemd/system/trivy-server.service

export TRIVY_SERVER_TOKEN=segredo-que-o-servidor-usara-para-verificar-os-tokens-JWT

sudo systemctl daemon-reload
sudo systemctl enable trivy-server.service
sudo systemctl start trivy-server.service
sudo systemctl status trivy-server.service

####################################################################################################

#gerando um JWT

pip install pyjwt

python3 trivy-jwt.py

trivy client --remote http://<ip-do-servidor>:4954 --token <token-jwt-gerado> image <nome-da-imagem>

