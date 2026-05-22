def process_user(body):
    username = body["username"]
    print(f"Processing user: {username}")
    return {
        "message": f"Hello {username}"
    }