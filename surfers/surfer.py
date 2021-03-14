from abc import abstractmethod


class Surfer:
    """A class of objects that surfs the internet"""

    @abstractmethod
    def get_target_name(self):
        """Returns the name of the target Site"""
        pass

    @abstractmethod
    def start_session(self):
        """Opens the browser and navigates to the target site (e.g. google.com)"""
        pass

    @abstractmethod
    def search(self, keyword):
        """Searches for keyword in the target site"""
        pass

    @abstractmethod
    def goto(self, keyword):
        """Navigates to sites containing keyword from within the target site"""
        pass

    def goto_all(self, keywords):
        """Goes to all of the addresses in addresses sequentially"""
        for keyword in keywords:
            self.goto(keyword)
            # todo - sleep? (=waiting period?)
            
    def end_session(self):
        """Ends the browsing session"""
        pass
