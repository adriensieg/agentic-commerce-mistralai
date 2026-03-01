from .tools import mcp
from .middleware import BearerAuthMiddleware
from .routes import (
    oauth_metadata,
    protected_resource_metadata,
    dynamic_client_registration,
    health_check,
    debug_token,
)