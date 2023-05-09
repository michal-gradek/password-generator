import src.generator.generator as generator
import src.parameters.parameters as params


def main():
    param = params.parameter()

    length = param.input_int_check("Podaj dlugosc hasła")
    uppercase = param.input_bool_check("Duże litery")
    lowercase = param.input_bool_check("Małe litery")
    number = param.input_bool_check("Cyfry")
    special = param.input_bool_check("Znaki specjalne")

    password = generator.passwordGenerator(length, lowercase, uppercase, special, number)

    try:
        pass_gen = password.generate()
        print(f"Generated password: {pass_gen}")
    except Exception as err:
        raise Exception(f"Error: {err}")


if __name__ == '__main__':
    main()
