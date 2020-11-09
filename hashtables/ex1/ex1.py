def get_indices_of_item_weights(weights, length, limit):
    if len(weights) < 2:
        return None

    weight_hash = {}

    for i in range(len(weights)):
        if limit - weights[i] in weight_hash:
            return (i, weight_hash[limit - weights[i]])
        weight_hash[weights[i]] = i

    return None
