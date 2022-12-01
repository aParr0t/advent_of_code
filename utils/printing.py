def static_print(string: str) -> None:
    print(string, end ="\r", flush=True)

def end_static_print() -> None:
    print('\n')