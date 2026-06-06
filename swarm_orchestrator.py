from agents import call_llm, TRIAGER_PROMPT, INVESTIGATOR_PROMPT, PATCHER_PROMPT, INSPECTOR_PROMPT
from mock_data import KNOWLEDGE_BASE

def execute_swarm_pipeline(incident_log: str):
    steps = []
    
    # Step 1: Triage
    triage_plan = call_llm(TRIAGER_PROMPT, f"Analyze this crash log:\n{incident_log}")
    steps.append({"agent": "Triager Agent", "output": triage_plan})
    
    # Step 2: Investigate
    matched_docs = KNOWLEDGE_BASE["database_pool.py"] + "\n" + KNOWLEDGE_BASE["CheckoutGateway"]
    analysis = call_llm(INVESTIGATOR_PROMPT, f"Plan: {triage_plan}\nRelevant Internal Docs:\n{matched_docs}")
    steps.append({"agent": "Log Investigator Agent", "output": analysis})
    
    # Step 3: Patch
    patch_code = call_llm(PATCHER_PROMPT, f"Write a code fix based on this analysis:\n{analysis}")
    steps.append({"agent": "Patch Engineer Agent", "output": patch_code})
    
    # Step 4: Validate
    qa_review = call_llm(INSPECTOR_PROMPT, f"Review this code fix:\n{patch_code}\nContext context:\n{analysis}")
    steps.append({"agent": "QA Inspector Agent", "output": qa_review})
    
    return steps