import pypandoc


def write_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)


def make_slides(path, type):
    if type == 'revealjs':
        return pypandoc.convert_file(path, to=type,
                                     extra_args=['-s', '-V', 'revealjs-url=http://lab.hakim.se/reveal-js'])
    elif type in ('slidy', 'dzslides'):
        return pypandoc.convert_file(path, to=type, extra_args=['-s'])
    else:
        return f'Type must be revealjs, slidy, or dzslides, not {type}'


write_file('slides.html', make_slides('slides.md', 'slidy'))
