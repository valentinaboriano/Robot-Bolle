from search import Problem


def is_valid(state):
    m, c, b = state
    result = not ((c > m > 0) or ((3 - c) > (3 - m) and m < 3))
    return result


def h(node):
    m, c, b = node.state
    return m + c - b


class MC(Problem):

    def value(self, state):
        pass

    def actions(self, state):
        if not is_valid(state):
            return []
        m, c, b = state
        result = []
        if b == 1:
            if m > 0:
                result.append('M->')
            if c > 0:
                result.append('C->')
            if m > 0 and c > 0:
                result.append('MC->')
            if m > 1:
                result.append('MM->')
            if c > 1:
                result.append('CC->')
        if b == 0:
            m = 3 - m
            c = 3 - c
            if m > 0:
                result.append('<-M')
            if c > 0:
                result.append('<-C')
            if m > 0 and c > 0:
                result.append('<-MC')
            if m > 1:
                result.append('<-MM')
            if c > 1:
                result.append('<-CC')
        return result

    def result(self, state, action):
        m, c, b = state
        if action == 'M->':
            return m - 1, c, 0
        if action == 'C->':
            return m, c - 1, 0
        if action == 'MM->':
            return m - 2, c, 0
        if action == 'CC->':
            return m, c - 2, 0
        if action == 'MC->':
            return m - 1, c - 1, 0
        if action == '<-M':
            return m + 1, c, 1
        if action == '<-C':
            return m, c + 1, 1
        if action == '<-MM':
            return m + 2, c, 1
        if action == '<-CC':
            return m, c + 2, 1
        if action == '<-MC':
            return m + 1, c + 1, 1
        else:
            raise Exception('action not found')




