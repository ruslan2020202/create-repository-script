from create_repository import NewRepository, ConnectRepository


def main() -> None:
    repository = NewRepository()
    con = ConnectRepository()
    if not con.search_repository(repository.path):
        repository.new_repository()
    con.connect()




if __name__ == "__main__":
    main()
