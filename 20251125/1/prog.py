class dump(type):
    def __new__(mcls, name, bases, namespace):
        new_ns = {}

        for attr, value in namespace.items():
            if callable(value):
                def make_wrapper(func, fname):
                    def wrapper(self, *args, **kwargs):
                        print(f"{fname}: {args}, {kwargs}")
                        return func(self, *args, **kwargs)
                    return wrapper

                new_ns[attr] = make_wrapper(value, attr)
            else:
                new_ns[attr] = value

        return super().__new__(mcls, name, bases, new_ns)


import sys
exec(sys.stdin.read())
