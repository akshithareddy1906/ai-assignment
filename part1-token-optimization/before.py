import time


def token_count(text):
    return len(text.split())


def planner(query):
    print("Planner is creating a plan...")
    time.sleep(0.5)

    return {
        "plan": "Research the topic and prepare an answer.",
        "tokens": token_count(query)
    }


def retriever(query):
    print("Retriever is searching documents...")
    time.sleep(0.5)

    return {
        "documents": [
            "Document 1",
            "Document 2",
            "Document 3"
        ],
        "tokens": token_count(query)
    }


def summarizer(query):
    print("Summarizer is generating summary...")
    time.sleep(0.5)

    return {
        "summary": "Generated summary from retrieved documents.",
        "tokens": token_count(query)
    }


def reviewer(query):
    print("Reviewer is checking the final answer...")
    time.sleep(0.5)

    return {
        "status": "Approved",
        "tokens": token_count(query)
    }


def run_pipeline(query):
    planner_result = planner(query)
    retriever_result = retriever(query)
    summarizer_result = summarizer(query)
    reviewer_result = reviewer(query)

    total_tokens = (
        planner_result["tokens"]
        + retriever_result["tokens"]
        + summarizer_result["tokens"]
        + reviewer_result["tokens"]
    )

    print("\nPipeline Summary")
    print("-" * 30)
    print(f"Planner Tokens     : {planner_result['tokens']}")
    print(f"Retriever Tokens   : {retriever_result['tokens']}")
    print(f"Summarizer Tokens  : {summarizer_result['tokens']}")
    print(f"Reviewer Tokens    : {reviewer_result['tokens']}")
    print("-" * 30)
    print(f"Total Tokens Used  : {total_tokens}")


if __name__ == "__main__":
    query = (
        "Explain Retrieval Augmented Generation, vector databases, embeddings, "
        "chunking strategies, prompt engineering, hallucination reduction, "
        "deployment architecture, monitoring and production best practices. "
    ) * 80

    run_pipeline(query)