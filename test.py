from daemonizer import Daemon


class daemon(Daemon):
    def run(self):
        print("Test Okay.")

daemon_object = daemon("./pid.pid")
daemon_object.start()
