

from analytics_engine import create_tracker
from user_manager import fetch_user_data


def main():
    # 1. Bind dependency once during setup
    track_user = create_tracker(fetch_user_func=fetch_user_data)

    # 2. Invoke operational function seamlessly without re-injecting the dependency
    track_user(101)
    track_user(102)

    # Handling missing user gracefully
    track_user(999)


if __name__ == "__main__":
    main()