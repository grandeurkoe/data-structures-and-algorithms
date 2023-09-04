def memoized_add_80_to_n():
    cache = {}

    def closure_memoized_add_80_to_n(n):
        if n in cache:
            print(f"Accessing {n} from cache. The value for {n} is {cache[n]}.")
        else:
            cache[n] = n + 80
            print(f"Adding {n} to cache with a value of {cache[n]}.")

    return closure_memoized_add_80_to_n


memoized = memoized_add_80_to_n()
memoized(5)
memoized(5)
