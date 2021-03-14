from surfers.surfer import Surfer


class GoogleSurfer(Surfer):

    TARGET = "https://www.google.com/"

    def get_target_name(self):
        return GoogleSurfer.TARGET

    def search(self, keyword):
        pass

    def goto(self, keyword):
        pass

    def start_session(self):
        pass
