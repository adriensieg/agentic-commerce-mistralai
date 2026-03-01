# Agentic Commerce Protocol

**What if you could place your order directly with Mistral AI Le Chat using the Agentic Commerce Protocol?**

We implemented a secure, **OAuth-protected MCP server** that enables **Mistral AI Le Chat** to **discover products**, **execute commerce tools**, and **complete end-to-end Agentic Commerce transactions** through a **standardized** and **trusted protocol**.

### Commerce Protocol
We implement an AI agent that enables users to discover products, negotiate, order, and pay within a standardized and seamless commerce flow.

### Secure Server Exposure
Le Chat connects to our OAuth-protected MCP server using **discovery Dynamic Client Registration (DCR)**, and a **PKCE Authorization Code flow** with **Auth0**. It obtains a **signed JWT access token**, verified via **JWKS** before **granting MCP-based MCP tool execution** with automatic token refresh.

### Capabilities
Secure **product discovery**, **contextual ordering**, **real-time negotiation**, **payment initiation** via CIBA, and persistent user context — enabling end-to-end trusted Agentic Commerce.

Just tell Le Chat what you want — and it orders, negotiates, and pays for you.

We implement a secure, OAuth-protected MCP server that enables Mistral AI Le Chat to discover products, execute commerce tools, and complete end-to-end Agentic Commerce transactions through a standardized and trusted protocol.

# OAuth 2.1 - Secure Server Exposure

```
agentic-commerce/
├── app.py
└── mcp_auth/
    ├── __init__.py
    ├── config.py
    ├── token.py
    ├── middleware.py
    ├── routes.py
    └── tools.py
```

# Capabilities