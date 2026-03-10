def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """

    set_a = set(set_a)
    set_b = set(set_b)

    union_size = len(set_a | set_b)

    if union_size == 0:
        return 0

    j = len(set_a & set_b) / union_size
    return j