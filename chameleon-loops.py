import os
import webbrowser

import chameleon


def generate():
    result_filename = 'loops.html'

    template = templates['loops.pt']
    result_html = template(
        title='Chameleon Loops',
        greetings='Welcome to Chameleon Loops example.',
        records={('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H')},
        summary=('May', 'The Force', 'be with you', 'always!')
    )
    print(result_html)

    result_file = open(result_filename, 'w')
    result_file.write(result_html)
    result_file.close()

    webbrowser.open(result_filename)


if __name__ == '__main__':
    path = os.path.dirname(__file__)
    templates = chameleon.PageTemplateLoader(os.path.join(path, "templates"))

    generate()
