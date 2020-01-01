"""
# Zadanie #11
Zaimplementuj klasy odpowiedzialne za tworzenie dokumentów w składni MarkDown. Stwórz klasę bazową `Element`
zawierającą podstawową implementację metody `render()` oraz kilka jej klas pochodnych. Stwórz klasę `Document`
umożliwiającą wyrenderowanie dodanych elementów.
Przykład użycia:
document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()
Header
======
[ABC](http://abc.com)
Simple
"""

class Element:

    def __init__(self,text: str):
        self.text = text

    def render(self):
        return self.text

class HeadElement(Element):
    def __init__(self, text, level: int = 1):
        self.text = text
        self.level = level
        return

    def render(self):
        text = super().render()
        if self.level == 1:
            return text.upper() + "\n" + 30*'='
        elif self.level == 2:
            return text + "\n" + 30*'-'
        else:
            return text + "\n"

class LinkElement(Element):
    def __init__(self,text,adress):
        self.text = text
        self.adress = adress

    def render(self):
        return 'http://'+ self.text.lower() + self.adress[self.adress.index("."):]

f = LinkElement('ABC', 'abc.com')

class Document():
    def __init__(self):
        self.text = ""

    def render(self):
        return self.text


def document_add_element(self):
    return self.render()

document = Document()

print(document_add_element(HeadElement('Netflix',2)))
print(document_add_element(Element('Nieograniczona oferta filmów, seriali, programów i nie tylko. Oglądaj wszędzie. Anuluj w każdej chwili.')))
print(document_add_element(LinkElement('Netflix', 'netflix.org')))

print("\n", 60*'*')

e = HeadElement(f"To jest nagłówek")
print(e.render())
e = HeadElement(f"To jest nagłówek",2)
print(e.render())
e = HeadElement(f"To jest nagłówek",3)
print(e.render())

print(f.render())
