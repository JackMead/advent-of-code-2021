import cProfile
import pstats
import functools

def add_profile(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        profile = cProfile.Profile()
        profile.enable()
        result = func(*args, **kwargs)
        profile.disable()
        ps = pstats.Stats(profile)
        ps.print_stats()
        return result
    return wrap