import stackImp


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['
    righty = ')}]'
    S = stackImp.ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


def is_matched_html(raw):
    """Return True if all HTML tags are property match; False otherwise """
    S = stackImp.ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()


if __name__ == "__main__":
    test1 = '({}{}())()'
    test2 = '{{{{{{[[[[[[{{{{{{((((([()])))))}}}}}}]]]]]]}}}}}}'
    print(is_matched(expr=test1), is_matched(expr=test2))

    test3 = """<body>
            <center>
            <h1> The Little Boat </h1>
            </center>
            <p> The storm tossed the little
            boat like a cheap sneaker in an
            old washing machine. The three
            drunken fishermen were used to
            such treatment, of course, but
            not the tree salesman, who even as
            a stowaway now felt that he
            had overpaid for the voyage. </p>
            <ol>
            <li> Will the salesman die? </li>
            <li> What color is the boat? </li>
            <li> And what about Naomi? </li>
            </ol>
            </body>"""
    print(is_matched_html(test3))