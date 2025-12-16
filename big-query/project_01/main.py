from shared.authentication import check_auth, get_client

from .queries import execute_queries

DRY_RUN = False


def main() -> None:
    print("Authenticating with Google Cloud...")
    check_auth()
    client = get_client()
    print("Starting query execution...")
    execute_queries(client, dry_run=DRY_RUN)
    print("Finished executing queries.")


if __name__ == "__main__":
    main()
