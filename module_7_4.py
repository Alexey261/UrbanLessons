#  %:
team1_num, team2_num = 5, 6
print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# format()
score_2 = 42
print('Команда "Волшебники данных" решила задач: {0} !'.format(score_2))
print('"Волшебники данных" решили задачи за: {team1_time:7.1f} с !'.format(team1_time=18015.15))

big_prise = 100000000000
win_team = 'Команда "Волшебники данных" получает приз: '
print('{}{:,} btc!!!'.format(win_team, big_prise))  # автоматическая нумерация полей для format()

# f-strings
score_1, score_2 = 40, 42
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'Победа команды "Мастера кода"!'
print(f'Результат битвы: {challenge_result}')
tasks_total, time_avg = 82, 45.212
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!')


