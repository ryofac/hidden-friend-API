from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin, YamlRenderPlugin

from presentation.routes.auth_route import auth_route

app = Litestar(
    route_handlers=[auth_route],
    on_startup=[],
    on_shutdown=[],
    openapi_config=OpenAPIConfig(
        title="HiddenFriendAPI",
        version="1.0.0",
        root_schema_site="swagger",
        render_plugins=[
            SwaggerRenderPlugin(path="/docs"),
            YamlRenderPlugin(path="/spec"),
        ],
    ),
)
