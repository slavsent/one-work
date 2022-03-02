tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Сава', 'Анна', 'Евгений'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_tutors(tutor, klass):
    for i in range(len(tutor)):
        if i >= len(klass):
            yield (tutor[i], None)
        else:
            yield (tutor[i], klass[i])


gen_tutors1 = ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None) for i in range(len(tutors)))

print(type(gen_tutors1))
print(type(gen_tutors(tutors, klasses)))

print(*gen_tutors1)
print(*gen_tutors(tutors, klasses))
