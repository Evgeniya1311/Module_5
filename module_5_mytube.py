class User:
    """
    Класс пользователя, содержащий уникальный логин, пароль (в хэшированном виде) и возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        # return f'{self.nickname}, {self.password}, {self.age}'
        return f'{self.nickname}'

class Video:
    """
    Класс видео, содержащий уникальное название, продолжительность (в сек),
    время остановки (по умол. = 0), ограничение по возрасту (по умол. = False)
    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __str__(self):
        return f'{self.title}, {self.duration}, {self.time_now}, {self.adult_mode}'

class UrTube:
    """
    Класс видеохостинга, имеющие следующие методы:
    register (имя, пароль, возраст) - регистрирует пользователя с УНИКАЛЬНЫМ логином в системе
    и сохраняет его в списке users
    log_in (имя, пароль) - выполняет вход в систему, меняет текущего пользователя при наличии его в списке
    log_out() - меняет текущего пользователя на None
    add(неограниченного кол-во объектов класса Video) - добавляет объекты в список videos с уникальным названием
    get_videos(строка) - находит совпадения с названиями видео в списке videos
    watch_video(точное название видео) - запускает просмотр видео при точном совпадении его названия с видео
    из списка videos, пройденном ограничении по возрасту 18+. Видео запускается с начала до точки стоп или до конца.
    """
    def __init__(self):
        self.users = [] #список объектов класса User
        self.videos = [] #список объектов класса Video
        self.current_user = None

    def register(self, name, password, age):
        if not self.users: #при первом запуске пополняем список первым объектом, чтобы могли по нему дальше искать
            user = User(name, password, age)
            self.users.append(user)
            self.current_user = user
        else:
            c = 0  # у меня только с использованием счетчика получилось :)
            for i in self.users:
                if name == i.nickname:
                    print(f'Пользователь {name} уже существует')
                    c += 1
            if c == 0: #если повторений имени нет, то создаем новый объект
                user1 = User(name, password, age)
                self.users.append(user1)
                self.current_user = user1

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname:
                if i.password == hash(password):
                    self.current_user = i

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            c = 0
            if not self.videos:
                self.videos.append(i)
            else:
                for j in self.videos:
                    if j.title == i.title:
                        c += 1
                if c == 0:
                    self.videos.append(i)

    def get_videos(self, finder):
        find = []
        for i in self.videos:
            if finder.upper() in i.title.upper():
                find.append(i.title)
        return find

    def watch_video(self, title_vid):
        from time import sleep
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if title_vid == i.title:
                    if i.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    else:
                        if i.time_now > 0:
                            for n in range(1, i.time_now+1):
                                print(n, end=' ')
                                sleep(0.5)
                            print('Конец видео')
                        else:
                            for n in range(1, i.duration+1):
                                print(n, end=' ')
                                sleep(0.5)
                            print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

