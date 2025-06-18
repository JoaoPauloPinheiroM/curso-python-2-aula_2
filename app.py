from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
restaurante_japones = Restaurante('Japonese food', "Japonesa")

restaurante_japones.alterar_estado()







def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()