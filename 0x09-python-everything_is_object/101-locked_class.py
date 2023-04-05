#!/usr/bin/python3

"""A locked class"""


class LockedClass:
    """A class with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name."""
    __slots__ = ["first_name"]

    def __setattr__(self, attr, fname):
        """Intercept attribute assignment attempts.
        Allow only attributes called "first_name" to be set.
        Raise AttributeError if any other attribute is assigned."""
        if not hasattr(self, attr) and attr != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute 'last_name'")
        super().__setattr__(attr, fname)
