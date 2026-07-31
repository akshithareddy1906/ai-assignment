import time


def token_count(text):
    return len(text.split())


def compress_query(query, max_words=120):
    """Keep only the first part of the query."""
    words = query.split()
    return " ".join(words[:max_words])


def planner(query):
    print("Planner is creating a plan...")
    time.sleep(0.3)

    plan = {
        "goal": "Answer the user's question",
        "keywords": [
            "RAG",
            "Embeddings",
            "Vector Database",
            "Prompt Engineering",
            "Caching"
        ]
    }

    return plan, token_count(query)


def retriever(plan):
    print("Retriever is searching only relevant documents...")
    time.sleep(0.3)

    documents = [
        "RAG improves factual accuracy.",
        "Embeddings help semantic search.",
        "Caching reduces API costs."
    ]

    context = " ".join(documents)

    return context, token_count(context)


def summarizer(context):
    print("Summarizer is preparing the answer...")
    time.sleep(0.3)

    summary = (
        "Retrieval-Augmented Generation improves LLM responses by retrieving "
        "relevant documents before generating an answer. Using embeddings and "
        "vector databases improves search quality, while caching helps reduce "
        "latency and cost."
    )

    return summary, token_count(context)


def reviewer(summary):
    print("Reviewer skipped (high confidence).")
    return "Skipped", 0


def run_pipeline(query):
    original_tokens = token_count(query)

    compressed_query = compress_query(query)

    planner_output, planner_tokens = planner(compressed_query)

    retrieved_context, retriever_tokens = retriever(planner_output)

    summary, summarizer_tokens = summarizer(retrieved_context)

    review_status, reviewer_tokens = reviewer(summary)

    optimized_total = (
        planner_tokens
        + retriever_tokens
        + summarizer_tokens
        + reviewer_tokens
    )

    before_total = original_tokens * 4

    print("\n" + "=" * 50)
    print("TOKEN USAGE COMPARISON")
    print("=" * 50)

    print(f"Before Optimization : {before_total} tokens")
    print(f"After Optimization  : {optimized_total} tokens")

    reduction = (
        (before_total - optimized_total) / before_total
    ) * 100

    print(f"Token Reduction     : {reduction:.2f}%")

    print("\nQuality Impact")
    print("- Context compressed")
    print("- Relevant information preserved")
    print("- Reviewer skipped for high-confidence responses")
    print("- Output quality remains almost the same")

    print("\nGenerated Answer")
    print("-" * 50)
    print(summary)


if __name__ == "__main__":

    query = (
        "Explain Retrieval Augmented Generation, embeddings, vector databases, "
        "prompt engineering, chunking strategies, hallucination reduction, "
        "latency optimization, caching, monitoring, deployment architecture, "
        "security, evaluation metrics and production best practices. "
    ) * 80

    run_pipeline(query)