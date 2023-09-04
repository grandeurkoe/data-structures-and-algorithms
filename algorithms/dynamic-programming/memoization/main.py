cache = {}


def memoized_add_80_to_n(n):
    if n in cache:
        print(f"Accessing {n} from cache. The value for {n} is {cache[n]}.")
    else:
        cache[n] = n + 80
        print(f"Adding {n} to cache with a value of {cache[n]}.")


memoized_add_80_to_n(5)
memoized_add_80_to_n(5)
