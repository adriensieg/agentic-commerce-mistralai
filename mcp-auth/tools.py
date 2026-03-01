from fastmcp import FastMCP

mcp = FastMCP("Mistral Hello World MCP Server")


@mcp.tool()
def search_products(query: str, max_price: float) -> str:
    """Search product catalog by natural language query and price ceiling. Returns JSON list of matching products with id, name, price, image_url."""


@mcp.tool()
def create_order(product_id: str, delivery_mode: str, customer_name: str, address: str) -> str:
    """Create a pending order in the system. Returns order_id and total amount."""


@mcp.tool()
def initiate_ciba_auth(order_id: str, phone_number: str) -> str:
    """Trigger a CIBA backchannel authentication request for a given order. Sends OTP via SMS. Returns auth_request_id."""


@mcp.tool()
def verify_ciba_otp(auth_request_id: str, otp: str) -> str:
    """Verify the OTP submitted by the user against the pending CIBA auth request. Returns verified: true/false."""


@mcp.tool()
def confirm_payment(order_id: str, auth_request_id: str) -> str:
    """Charge the customer's registered payment method once CIBA auth is confirmed. Returns confirmation_code and receipt_url."""