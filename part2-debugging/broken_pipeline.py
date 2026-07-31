import json
import random
import time


def planner(query):
    print("Planner: Creating execution plan...")
    time.sleep(1)

    return {
        "task": "answer_question",
        "query": query
    }


def retriever(plan):
    print("Retriever: Fetching documents...")
    time.sleep(1)

    # Simulate random timeout
    if random.choice([False, False, True]):
        raise TimeoutError("Retriever service timed out.")

    return [
        "RAG improves factual accuracy.",
        "Embeddings help semantic search.",
        "Vector databases enable fast retrieval."
    ]


def summarizer(documents):
    print("Summarizer: Generating response...")
    time.sleep(1)

    # Simulate malformed JSON response
    if random.choice([False, True, False]):
        return '{"answer": "RAG improves accuracy"'  # Missing closing brace

    response = {
        "answer": "RAG improves LLM accuracy by retrieving relevant documents before generation."
    }

    return json.dumps(response)


def reviewer(response):
    print("Reviewer: Checking response...")
    time.sleep(1)

    # Simulate silent incorrect data
    if random.choice([False, False, True]):
        return {
            "status": "success",
            "answer": "RAG is a database."   # Wrong answer but marked successful
        }

    return {
        "status": "success",
        "answer": response["answer"]
    }


def run_pipeline(query):
    try:
        plan = planner(query)

        docs = retriever(plan)

        summary = summarizer(docs)

        try:
            summary = json.loads(summary)
        except json.JSONDecodeError:
            print("\nERROR: Invalid JSON received from Summarizer.")
            return

        result = reviewer(summary)

        print("\nPipeline Result")
        print("------------------------------")
        print("Status :", result["status"])
        print("Answer :", result["answer"])

    except TimeoutError as e:
        print("\nTIMEOUT ERROR")
        print(e)

    except Exception as e:
        print("\nUnexpected Error")
        print(e)


if __name__ == "__main__":
    query = "Explain Retrieval Augmented Generation."

    run_pipeline(query)