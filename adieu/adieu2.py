"""
In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu
Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu
To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d.
Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and  names with  commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""

# load library
import inflect


# looping to add inputs to a list
def main():
    names_ls = []
    while True:
        try:
            name = ask("Name: ")
            if len(name) > 0:
                names_ls.append(name)
        except EOFError:
            break
    print("Adieu, adieu, to", inflect.engine().join(names_ls))


# ask user for inputs
def ask(a):
    return str(input(a)).capitalize()


if __name__ == "__main__":
    main()
