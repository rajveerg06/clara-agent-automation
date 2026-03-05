def generate_changelog(v1, v2):

    changes = {}

    # check keys from both versions
    all_keys = set(v1.keys()).union(set(v2.keys()))

    for key in all_keys:

        if v1.get(key) != v2.get(key):

            changes[key] = {
                "old": v1.get(key),
                "new": v2.get(key)
            }

    return changes