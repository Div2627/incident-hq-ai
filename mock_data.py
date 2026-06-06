# Simulated real-time server error log that triggers the swarm
MOCK_INCIDENT_LOG = """
[2026-06-06 19:15:22] ERROR: database_pool.py - Connection Pool Exhausted. 
Active connections: 100/100. Timeout waiting for free connection.
Affected Service: CheckoutGateway API v2.
"""

# Simulated internal engineering documentation for the RAG lookup tool
KNOWLEDGE_BASE = {
    "database_pool.py": "Standard fix for connection pool exhaustion: Check if session closures are missing in the checkout router context, or increase MAX_POOL_SIZE in config if traffic spikes.",
    "CheckoutGateway": "CheckoutGateway uses SQLAlchemy sessions. Every database session must explicitly call db.close() inside a try/finally block."
}