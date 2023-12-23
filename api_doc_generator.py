from fastapi.openapi.utils import get_openapi
import yaml

from api.server import app

openapi_schema = get_openapi(
    title="Wallet Warden Server",
    version="1.0.0",
    description="Wallet Warden API",
    routes=app.routes,
)

with open('api_schema.yaml', 'w') as file:
    yaml.dump(openapi_schema, file)
