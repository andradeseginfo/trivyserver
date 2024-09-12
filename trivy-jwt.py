import jwt

# Segredo usado no servidor (mesmo valor de TRIVY_SERVER_TOKEN)
secret = "segredo-que-o-servidor-usara-para-verificar-os-tokens-JWT"

# Dados que podem ser codificados no token (payload)
payload = {
    "sub": "trivy-client",
    "name": "cliente-api",
    "iat": 1609459200  # Timestamp de emissão do token
}

# Gerar o token JWT
token = jwt.encode(payload, secret, algorithm="HS256")

print(token)
