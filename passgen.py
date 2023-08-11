"""
passgen.py

This module provides a function for generating
passwords with user-specified parameters.
"""


import random
import string
import sys


def password_generator(len_pass=8, use_letters=True,
                       use_numbers=True, use_punt=True):
    """Generate a password with the specified parameters."""
    options = ""

    if use_letters:
        options += string.ascii_letters

    if use_numbers:
        options += string.digits

    if use_punt:
        options += string.punctuation

    if not options:
        print("Você não definiu nenhum parâmetro para a sua senha")
        sys.exit()

    generated_pass = "".join(random.choice(options) for _ in range(len_pass))
    print(generated_pass)


def get_user_input(prompt, valid_options):
    '''Check if input is valid'''
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_options:
            return user_input
        print("Opção inválida!")


while not (length := input("Digite o tamanho da senha ou tecle \
enter para usar o tamanho padrão: ")).isdigit():
    print("Opção inválida!")

letters = get_user_input("Deseja usar letras em sua senha? (S/N) ", ("S", "N"))
numbers = get_user_input(
    "Deseja usar números em sua senha? (S/N) ", ("S", "N"))
punt = get_user_input(
    "Deseja usar caracteres especiais em sua senha? (S/N) ", ("S", "N"))

password_generator(int(length), letters == "S", numbers == "S", punt == "S")
