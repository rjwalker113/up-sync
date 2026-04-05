def compare_files(local, network):
    if not network.exists:
        return {"state": "missing_network"}

    if not local.exists:
        return {"state": "missing_local"}

    if local.size != network.size:
        return {"state": "size_mismatch"}

    if local.modified != network.modified:
        return {"state": "timestamp_mismatch"}

    # optional: hash comparison
    if local.hash != network.hash:
        return {"state": "hash_mismatch"}

    return {"state": "in_sync"}