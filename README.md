# Trivy Server
Instalação do Trivy em Modo Server

#atualiza servidor
sudo apt-get update
sudo apt-get install -y wget

#baixa arquivo do repositório (verificar versão mais atualizada)
wget https://github.com/aquasecurity/trivy/releases/download/v0.55.1/trivy_0.55.1_Linux-64bit.deb
sudo dpkg -i trivy_0.55.1_Linux-64bit.deb

#valida instalação
trivy --version

#cria serviço (codigo no repo)
sudo nano /etc/systemd/system/trivy-server.service

#exporta o segredo que será utilizado no jwt
export TRIVY_SERVER_TOKEN=segredo-que-o-servidor-usara-para-verificar-os-tokens-JWT

#inicia o serviço
sudo systemctl daemon-reload
sudo systemctl enable trivy-server.service
sudo systemctl start trivy-server.service
sudo systemctl status trivy-server.service

#gerando um JWT

#instala a dependencia do pyjwt
pip install pyjwt

#executa o codigo para gerar o token (codigo no repo)
python3 trivy-jwt.py
#obs.: precisa colocar o mesmo segredo que foi especificado no TRIVY_SERVER_TOKEN dentro codigo

trivy client --remote http://<ip-do-servidor>:4954 --token <token-jwt-gerado> image <nome-da-imagem>

