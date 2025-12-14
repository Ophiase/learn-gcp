from gsod_requests import filter_and_aggregation

from shared.authentication import check_auth, get_client


def main() -> None:
    check_auth()
    client = get_client()

    filter_and_aggregation(client)


if __name__ == "__main__":
    main()
