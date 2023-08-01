from google_api.connection import ConnectGoogleAPI


class Main:
    @staticmethod
    def main():
        google_api = ConnectGoogleAPI()
        google_api.get_credentials()
        google_api.get_labels()


if __name__ == '__main__':
    Main.main()
