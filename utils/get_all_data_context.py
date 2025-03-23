def get_all_data_context(datasets: dict) -> str:
    """
    Converts all datasets into a string format and concatenates them.
    """
    contexts = []
    for name, df in datasets.items():
        contexts.append(f"Dataset '{name}':\n" + df.to_string(index=False))
    return "\n\n".join(contexts)