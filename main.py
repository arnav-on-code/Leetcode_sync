from config.settings import Config

from sync.manager import SyncManager

from utils.formatter import display_banner


def main():

    Config.validate()
    Config.initialize()

    display_banner()

    manager = SyncManager()

    manager.run()


if __name__ == "__main__":
    main()