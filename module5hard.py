from time import sleep


class User:

    def __str__(self):
        class_name = str(self.__class__)
        class_name = class_name[class_name.index('.') + 1:-2]
        return f'Объект класса <{class_name}>, Имя: {self.nickname}, Возраст: {self.age}'

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title.casefold()
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        class_name = str(self.__class__)
        class_name = class_name[class_name.index('.') + 1:-2]
        return f'Объект класса: <{class_name}> "{self.title}", Длмтельность: {self.duration} c,' \
               f' {"для взрослых" if self.adult_mode else "без ограничений"}'


class UrTube:
    videos = []
    users = []
    current_user = None

    def add(self, *args):
        for i in range(len(args)):
            if not self._search(args[i].title, self.videos, 'title'):
                self.videos.append(args[i].__dict__)
        # print(self.videos)

    def _search(self, _name, _lst, _key):
        _found = False
        for _itm in _lst:
            if _itm[_key] == _name:
                _found = _itm
                break
        return _found

    def watch_video(self, vname):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео!')
        elif self.current_user.age <= 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу!')
        else:
            _flag = self._search(vname.casefold(), self.videos, 'title')
            if _flag:
                print(f'Смотрим \"{_flag["title"].capitalize()}\" ')
                self._timing(_flag['duration'])

    def _timing(self, time_sec):
        for i in range(1, time_sec + 1):
            sleep(0.5)
            print(str(i) + ' ', end='')
        print('Конец видео')

    def register(self, nickname, password, age):
        if not self._search(nickname, self.users, 'nickname'):
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user.__dict__)
        else:
            print(f'Пользователь {nickname} уже существует!')
        # print(self.users)

    def log_in(self, nickname, password):
        _cond1 = self._search(nickname, self.users, 'nickname')
        _cond2 = self._search(hash(password), self.users, 'password')
        if _cond1 and _cond2:
            new_user = User(nickname, password, _cond2['age'])
            if new_user == self.current_user:
                print(f'Пользователь {nickname} уже в системе!')
            else:
                self.current_user = new_user
        else:
            print('Ошибка входа в аккаунт!')

    def log_out(self):
        for i in range(len(self.users)):
            if self.users[i]['nickname'] == self.current_user.nickname:
                del self.users[i]
        self.current_user = None


    def get_videos(self, _str):
        _rez = []
        for i in self.videos:
            if _str.casefold() in i['title']:
                _rez.append(i['title'].capitalize())
        return _rez


ur = UrTube()
u1 = User('al', '123', 18)

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)




