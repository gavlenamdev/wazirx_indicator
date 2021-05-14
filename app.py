import sys

from wazirx_indicator import MyApplication

if __name__ == "__main__":
    app = MyApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
