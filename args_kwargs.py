
def volume(*lengths):
    it = iter(lengths)
    v = 1 if lengths else 0
    print("Lengths:", lengths)
    for length in it:
        v *= length

    return v


def html_tag(name, **kwargs):
    s = ''
    for k,v in kwargs.items():
        s += f'{k}="{v}" '
    print(f'<{name}', s, f'></{name}>')


def fix_number_pos_args_mandatory_kwargs(fname, lname, *, age, location):
    print(f"Name: {fname} {lname}")
    print(f"Age: {age}")
    print(f"Location: {location}")


# Extended Call Syntax: Passing positional args
def dbgprint(*args):
    print("\nDEBUG:", *args)


if __name__ == '__main__':
    print("Test Args:")
    print("Case 1: Single Arg:")
    print(volume(12))

    print("Case 2: Multiple Args:")
    print(volume(23, 45, 67))

    print("Case 3: Zero Args:")
    print(volume())

    print("\nTest kwargs:")
    html_tag("img", src="example.jpg", alt="A good example", border=2)
    html_tag("a", href="/root/product.html")
    html_tag("table", klass="main", style="table.css")

    dbgprint("Test Print...")
