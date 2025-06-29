from abc import ABC, abstractmethod
from typing import List

# --------- Profile class (represents a user in the network) ----------
class Profile:
    def __init__(self, profile_id: str, name: str, email: str, company: str, friends: List[str]):
        self.id = profile_id
        self.name = name
        self.email = email
        self.company = company
        self.friends = friends

    def __repr__(self):
        return f"{self.name} ({self.email})"


# --------- Iterator Interface ----------
class ProfileIterator(ABC):
    @abstractmethod
    def has_more(self) -> bool:
        pass

    @abstractmethod
    def get_next(self) -> Profile:
        pass


# --------- Concrete Iterator ----------
class FacebookIterator(ProfileIterator):
    def __init__(self, facebook, profile_id: str, type_: str):
        self.facebook = facebook
        self.profile_id = profile_id
        self.type = type_  # "friends" or "coworkers"
        self.current_position = 0
        self.cache = []
        self._lazy_load()

    def _lazy_load(self):
        profile = self.facebook.find_profile_by_id(self.profile_id)
        if not profile:
            return

        if self.type == "friends":
            self.cache = self.facebook.get_profiles(profile.friends)
        elif self.type == "coworkers":
            all_friends = self.facebook.get_profiles(profile.friends)
            self.cache = [p for p in all_friends if p.company == profile.company]

    def has_more(self) -> bool:
        return self.current_position < len(self.cache)

    def get_next(self) -> Profile:
        if self.has_more():
            profile = self.cache[self.current_position]
            self.current_position += 1
            return profile
        return None


# --------- Collection Interface ----------
class SocialNetwork(ABC):
    @abstractmethod
    def create_friends_iterator(self, profile_id: str) -> ProfileIterator:
        pass

    @abstractmethod
    def create_coworkers_iterator(self, profile_id: str) -> ProfileIterator:
        pass


# --------- Concrete Collection ----------
class Facebook(SocialNetwork):
    def __init__(self, profiles: List[Profile]):
        self.profiles = {p.id: p for p in profiles}

    def find_profile_by_id(self, profile_id: str) -> Profile:
        return self.profiles.get(profile_id)

    def get_profiles(self, ids: List[str]) -> List[Profile]:
        return [self.profiles[id_] for id_ in ids if id_ in self.profiles]

    def create_friends_iterator(self, profile_id: str) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id: str) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "coworkers")


# --------- Client Code (Spammer) ----------
class SocialSpammer:
    def send(self, iterator: ProfileIterator, message: str):
        while iterator.has_more():
            profile = iterator.get_next()
            print(f"Sending '{message}' to {profile.email}")


# --------- Application Setup ----------
def main():
    # Sample Data
    profiles = [
        Profile("1", "Alice", "alice@abc.com", "ABC Corp", ["2", "3"]),
        Profile("2", "Bob", "bob@abc.com", "ABC Corp", ["1"]),
        Profile("3", "Charlie", "charlie@xyz.com", "XYZ Ltd", ["1"]),
        Profile("4", "David", "david@abc.com", "ABC Corp", ["1", "2"]),
    ]

    facebook = Facebook(profiles)
    spammer = SocialSpammer()

    print("Send spam to friends of Alice:\n")
    friends_iterator = facebook.create_friends_iterator("1")
    spammer.send(friends_iterator, "Hi! This is a spam message.")

    print("\nSend spam to coworkers of Alice:\n")
    coworkers_iterator = facebook.create_coworkers_iterator("1")
    spammer.send(coworkers_iterator, "Meeting at 3PM today!")


if __name__ == "__main__":
    main()
