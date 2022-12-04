from enum import Enum


class TheirPlays(Enum):
    Rock = 'A'
    Paper = 'B'
    Scissors = 'C'


class OurPlays(Enum):
    Rock = 'X'
    Paper = 'Y'
    Scissors = 'Z'


match_scores = {
    TheirPlays.Rock: {
        OurPlays.Rock: 3,
        OurPlays.Paper: 6,
        OurPlays.Scissors: 0,
    },
    TheirPlays.Paper: {
        OurPlays.Rock: 0,
        OurPlays.Paper: 3,
        OurPlays.Scissors: 6,
    },
    TheirPlays.Scissors: {
        OurPlays.Rock: 6,
        OurPlays.Paper: 0,
        OurPlays.Scissors: 3,
    },
}
move_scores = {'X': 1, 'Y': 2, 'Z': 3}
outcomes = {'X': 0, 'Y': 3, 'Z': 6}  # loose, draw, win

file = open('input.txt', 'r')
lines = file.readlines()

score = 0
score_pt2 = 0

for line in lines:
    parts = line.strip().split(' ')

    theirs = TheirPlays(parts[0])
    ours = OurPlays(parts[1])

    score += match_scores[theirs][ours] + move_scores[parts[1]]

    if theirs == TheirPlays.Rock:
        if parts[1] == 'X': # Loose
            score_pt2 += match_scores[theirs][OurPlays.Scissors] + move_scores['Z']
        elif parts[1] == 'Y': # Draw
            score_pt2 += match_scores[theirs][OurPlays.Rock] + move_scores['X']
        elif parts[1] == 'Z': # Win
            score_pt2 += match_scores[theirs][OurPlays.Paper] + move_scores['Y']

    elif theirs == TheirPlays.Paper:
        if parts[1] == 'X': # Loose
            score_pt2 += match_scores[theirs][OurPlays.Rock] + move_scores['X']
        elif parts[1] == 'Y': # Draw
            score_pt2 += match_scores[theirs][OurPlays.Paper] + move_scores['Y']
        elif parts[1] == 'Z': # Win
            score_pt2 += match_scores[theirs][OurPlays.Scissors] + move_scores['Z']

    elif theirs == TheirPlays.Scissors:
        if parts[1] == 'X': # Loose
            score_pt2 += match_scores[theirs][OurPlays.Paper] + move_scores['Y']
        elif parts[1] == 'Y': # Draw
            score_pt2 += match_scores[theirs][OurPlays.Scissors] + move_scores['Z']
        elif parts[1] == 'Z': # Win
            score_pt2 += match_scores[theirs][OurPlays.Rock] + move_scores['X']

assert score == 10816
assert score_pt2 == 11657

print(f'End score: {score}')
print(f'Pt2 score: {score_pt2}')


