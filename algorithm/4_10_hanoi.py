def moveTower(level, fromPole, withPole, toPole):
    if level >= 1:
        moveTower(level-1, fromPole, toPole, withPole)
        print('move disk from {} to {}'.format(fromPole, toPole))
        moveTower(level-1, withPole, toPole, fromPole)

moveTower(5, 'A', 'B', 'C')