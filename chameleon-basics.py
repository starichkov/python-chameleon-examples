import os

path = os.path.dirname(__file__)

from chameleon import PageTemplateLoader

templates = PageTemplateLoader(os.path.join(path, "templates"))


def generate():
    template = templates['basics.pt']
    result_html = template(
        title='Chameleon Basics',
        greetings='Welcome to Chameleon',
    )
    print(result_html)

    result_file = open('basics.html', 'w')
    result_file.write(result_html)
    result_file.close()


if __name__ == '__main__':
    generate()
