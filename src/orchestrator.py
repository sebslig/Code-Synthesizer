import os
from typing import Dict, Any
from src.agents.spec_agent import SpecAgent
from src.agents.coder_agent import CoderAgent
from src.agents.qa_agent import QAAgent

class CodeGenOrchestrator:
    """Orchestrates the multi-agent workflow for code generation."""
    
    def __init__(self):
        self.spec_agent = SpecAgent()
        self.coder_agent = CoderAgent()
        self.qa_agent = QAAgent()

    def run(self, prompt: str) -> Dict[str, Any]:
        print(f"[Orchestrator] Starting task: {prompt}")
        
        # Phase 1: Specification
        spec = self.spec_agent.process(prompt)
        print("[Orchestrator] Specification generated.")
        
        # Phase 2: Implementation
        code = self.coder_agent.generate(spec)
        print("[Orchestrator] Code implementation complete.")
        
        # Phase 3: Validation
        test_results = self.qa_agent.verify(code, spec)
        
        if not test_results["success"]:
            print("[Orchestrator] Tests failed. Retrying implementation...")
            code = self.coder_agent.refine(code, test_results["errors"])
            test_results = self.qa_agent.verify(code, spec)
            
        return {
            "code": code,
            "tests": test_results["test_suite"],
            "status": "success" if test_results["success"] else "failed"
        }
