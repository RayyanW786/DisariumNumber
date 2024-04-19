from typing import List, Tuple


def resolve_power(index: int, number: int) -> int:
    return number ** index


def resolve_disarium(user: str, numbers: List[int]) -> Tuple[int, List[str], bool]:
    resolved_value = 0
    mapper: List[str] = []
    for idx, number in enumerate(numbers, start=1):
        resolved_value += resolve_power(idx, number)
        mapper.append(f"{number}**{idx}")
    return resolved_value, mapper, str(resolved_value) == user_input


while True:
    user_input: str = input(
        "enter your number: "
    )
    try:
        valid_numbers: int = int(user_input)
        valid_numbers: List[int] = [int(e) for e in str(valid_numbers)]
    except ValueError:
        print("Invalid Number")
        continue
    value, mapping, pred = resolve_disarium(user_input, valid_numbers)
    print(f"Your number is {'NOT ' if not pred else ''}a disarium number"
          f" {(' + '.join(mapping) + ' = ' + str(value)) if pred else ''}\n")
