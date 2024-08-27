class Book:

  def __init__(self, title: str, pages: int) -> None:
    self.title = title
    self.pages = pages

  def __format__(self, format_spec) -> str:
    match format_spec:
      case 'time':
        return f'{self.pages/60:.2f}h'
      case 'caps':
        return self.title.upper()
      case _:
        raise ValueError(f"Uknown specifier for Book()")


def main() -> None:
  hairy_potter: Book = Book('Very Hairy Potter', 300)
  python_daily: Book = Book('Python Daily', 20)

  print(f'{hairy_potter:caps}')  # Specifier: caps
  print(f'Read Time: {hairy_potter:time}')  # Specifier: caps


if __name__ == '__main__':
  main()
