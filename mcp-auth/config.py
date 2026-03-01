import os

AUTH0_DOMAIN        = os.environ.get("AUTH0_DOMAIN",        "dev-rcc43qlv8opam0co.us.auth0.com")
AUTH0_AUDIENCE      = os.environ.get("AUTH0_AUDIENCE",      "https://mistralai.devailab.work/mcp")
AUTH0_CLIENT_ID     = os.environ.get("AUTH0_CLIENT_ID",     "vy8sJbRt4cHMnUBmVkDO66NaBk6XUsgB")
AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET", "")
MCP_SERVER_URL      = os.environ.get("MCP_SERVER_URL",      "https://mistralai.devailab.work")
MISTRAL_REDIRECT    = "https://callback.mistral.ai/v1/integrations_auth/oauth2_callback"
JWKS_URL            = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
ISSUER              = f"https://{AUTH0_DOMAIN}/"