class controller:
    @staticmethod
    def format_number_for_BR(num):
        numero = num
        for key,i in enumerate(num):
            if not i.isdigit() :

                if (i == "." or i == ",") and key > 0:

                    numero = numero.replace(",",".")
                else:
                    raise ValueError("Digite um numero valido")
        return numero
            # elif not (i == "-" and key == 0) :
                # raise ValueError("Digite um numero valido")

