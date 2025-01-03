class parameter:

    def __init__(self):
        pass

    def input_bool_check(self, question):
        while True:
            value = input(f'{question} ? [t/f]').strip().lower()

            if value == 't':
                return True
            elif value == 'f':
                return False
            else:
                print('Please answer with yes or no!')

    def input_int_check(self, question):
        while True:
            query = input(f'{question}: ').strip()

            try:
                val = int(query)
                return val
            except ValueError:
                print(f"The entered value {query} is not a number")
                continue;
