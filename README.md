# Trivy Server
<br />Instalação do Trivy em Modo Server

#atualiza servidor
<br />sudo apt-get update
<br />sudo apt-get install -y wget

#baixa arquivo do repositório (verificar versão mais atualizada)
<br />wget https://github.com/aquasecurity/trivy/releases/download/v0.55.1/trivy_0.55.1_Linux-64bit.deb
<br />sudo dpkg -i trivy_0.55.1_Linux-64bit.deb

#valida instalação
<br />trivy --version

#cria serviço (codigo no repo)
<br />sudo nano /etc/systemd/system/trivy-server.service

#exporta o segredo que será utilizado no jwt
<br />export TRIVY_SERVER_TOKEN=segredo-que-o-servidor-usara-para-verificar-os-tokens-JWT

#inicia o serviço
<br />sudo systemctl daemon-reload
<br />sudo systemctl enable trivy-server.service
<br />sudo systemctl start trivy-server.service
<br />sudo systemctl status trivy-server.service

#gerando um JWT

#instala a dependencia do pyjwt
<br />pip install pyjwt

#executa o codigo para gerar o token (codigo no repo)
<br />python3 trivy-jwt.py
<br />#observação: precisa colocar o mesmo segredo que foi especificado no TRIVY_SERVER_TOKEN dentro codigo

trivy client --remote http://<ip-do-servidor>:4954 --token <token-jwt-gerado> image <nome-da-imagem>

