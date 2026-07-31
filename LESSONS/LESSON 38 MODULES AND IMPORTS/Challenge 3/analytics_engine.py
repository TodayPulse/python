
def create_tracker(fetch_user_func):

    def track_session(user_id: int):
        user_data = fetch_user_func(user_id)

        if not user_data:
            print(f"[Analytics] Track Failed: User {user_id} not found.")
            return None

        # Process analytics payload with bound data
        print(f"[Analytics] Tracking session for: {user_data['name']}")
        print(
            f"[Analytics] Event: Page View | Status: {user_data['status']}\n"
        )

        return {
            "user_id": user_id,
            "user_name": user_data["name"],
            "event": "page_view",
        }

    return track_session