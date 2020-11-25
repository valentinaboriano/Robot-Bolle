from search import Problem


def h(node):
    eye, snap, star, wave, exp, hide, ymca, fist, time, goal = node.state
    return goal - time


EYE, SNAP, STAR, WAVE, EXP, HIDE, YMCA, FIST, PAUSE = range(9)
TIMES = [500, 800, 360, 700, 408, 500, 936, 800, 1]

class A(Problem):
    def value(self, state):
        pass

    def result(self, state, action):
        eye, snap, star, wave, exp, hide, ymca, fist, time, goal = state
        index = PAUSE
        if 'eye' in action:
            eye = 1 - eye
            index = EYE
        if 'snap' in action:
            snap = 1 - snap
            index = SNAP
        if 'star' in action:
            star = 1 - star
            index = STAR
        if 'wave' in action:
            wave = 1 - wave
            index = WAVE
        if 'exp' in action:
            exp = 1 - exp
            index = EXP
        if 'hide' in action:
            hide = 1 - hide
            index = HIDE
        if 'ymca' in action:
            ymca = 1 - ymca
            index = YMCA
        if 'fist' in action:
            fist = 1 - fist
            index = FIST
        if 'pause' in action:
            index = PAUSE
        time += TIMES[index]
        return eye, snap, star, wave, exp, hide, ymca, fist, time, goal

    def actions(self, state):
        eye, snap, star, wave, exp, hide, ymca, fist, time, goal = state
        result = ['pause']
        if eye and time + TIMES[EYE] <= goal:
            result.append('eye')
        if snap and time + TIMES[SNAP] <= goal:
            result.append('snap')
        if star and time + TIMES[STAR] <= goal:
            result.append('star')
        if wave and time + TIMES[WAVE] <= goal:
            result.append('wave')
        if exp and time + TIMES[EXP] <= goal:
            result.append('exp')
        if hide and time + TIMES[HIDE] <= goal:
            result.append('hide')
        if ymca and time + TIMES[YMCA] <= goal:
            result.append('ymca')
        if fist and time + TIMES[FIST] <= goal:
            result.append('fist')
        return result

    def path_cost(self, c, state1, action, state2):
        if 'pause' in action:
            return c+1
        else:
            return c

    def goal_test(self, state):
        eye, snap, star, wave, exp, hide, ymca, fist, time, goal = state
        if time == goal:
            return True
        else:
            return False
