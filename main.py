from src.orchestrator import CodeGenOrchestrator
import sys

def main():
    if len(sys.argv) < 2:
        prompt = "Write a function that parses a CSV string into a list of dictionaries."
    else:
        prompt = " ".join(sys.argv[1:])

    print(f"--- Code Generation Agent ---")
    orchestrator = CodeGenOrchestrator()
    result = orchestrator.run(prompt)
    
    print("\n--- GENERATED CODE ---")
    print(result['code'])
    print("\n--- TEST SUITE ---")
    print(result['tests'])

if __name__ == "__main__":
    main()
