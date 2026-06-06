# --- AGENT PROMPT VARIABLE NAMES (Required by Orchestrator) ---
TRIAGER_PROMPT = "SWARM_TRIAGER"
INVESTIGATOR_PROMPT = "LOG_INVESTIGATOR"
PATCHER_PROMPT = "PATCH_ENGINEER"
INSPECTOR_PROMPT = "QA_INSPECTOR"

def call_llm(agent_role: str, user_content: str) -> str:
    """
    Local Deterministic AI Engine. 
    Simulates high-fidelity multi-agent reasoning loops instantly without API keys.
    """
    if "SWARM_TRIAGER" in agent_role:
        return """[INTERNAL REASONING LOOP: SEVERITY CRITICAL]
Analysis of incoming string payload completed.
Target Error: Connection Pool Exhausted inside 'database_pool.py'.
Affected Subsystem: CheckoutGateway API v2.

INVESTIGATION ROADMAP DEPLOYED:
1. Locate unclosed sessions inside the Checkout Gateway router context.
2. Verify if try/finally blocks are explicitly releasing connections back to the core manager.
3. Formulate temporary environment patch to dynamically scale MAX_POOL_SIZE."""

    elif "LOG_INVESTIGATOR" in agent_role:
        return """[CROSS-REFERENCING INTERNAL DOCUMENTATION... MATCH FOUND]
Target File: CheckoutGateway / database_pool.py
Root Cause Identified: In 'CheckoutGateway API v2', asynchronous routes are initializing SQLAlchemy database sessions but failing to call 'db.close()' upon completing transactions. 
Result: Active pools hit the ceiling threshold of 100/100 connections within minutes of high checkout traffic spikes, locking out incoming users."""

    elif "PATCH_ENGINEER" in agent_role:
        return """// PROPOSED HOTFIX PATCH FOR: CheckoutGateway/router.py
// TARGET: Wrap database context lifecycle management safely

import database_pool as db

def process_checkout_transaction(user_payload):
    session = db.get_session()
    try:
        # Core checkout execution logic
        result = db.execute_checkout(session, user_payload)
        session.commit()
        return {"status": "success", "data": result}
    except Exception as error:
        session.rollback()
        raise error
    finally:
        # CRITICAL FIX: Ensures connection is ALWAYS returned to the pool
        session.close() 
        print("[SWARM HOTFIX] Database connection context successfully returned to pool.")"""

    elif "QA_INSPECTOR" in agent_role:
        return """[SWARM SECURITY & QUALITY EVALUATION INTERPOLATION]
Reviewing Patch: 'CheckoutGateway/router.py'
Syntax Check: VALID (Python AST structure intact)
Security Profile: SAFE. The injection of the explicit 'finally' block ensures database session release under all runtime failure paradigms.

DECISION STATUS: APPROVED
Action: Deployment pipeline authorized. Incident state set to RESOLVED."""
    
    return "Agent processing completed successfully."