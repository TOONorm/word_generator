from generator import Words_generator as Wg
import time
import os


def get_settings():
    return print(stt.lang_settings)

def set_gen_settings():
    count = int(input("Введите кол-во выводимых слов за раз:\n"))
    ln_wrd = int(input("Длинна слова: "))
    print("Введите наличие или отсутсвие частей слова\n1 -- если есть\n0 -- если нет")
    pref = int(input("Приставка: "))
    suff = int(input("Суффиксы: "))
    end = int(input("Окончания: "))
    return (count,ln_wrd,pref,suff,end)

def get_gen_settings():
    print(f'Кол-во слов: {setting[count]}\n'
          f'Длинна слов: {setting[ln_wrd]}\n'
          f'Приставки: {setting[pref]}\n'
          f'Суффиксы: {setting[suff]}\n'
          f'Окончания: {setting[end]}')

def del_settings():
    enter = input("Вы уверены? yes/no\n")
    if enter == 'yes':
        place = os.path.abspath('lists.py')
        os.remove(place)
        print("Файл удалён!\nПриложение закроется через 5 секунд")
        time.sleep(5)
        raise KeyboardInterrupt


try:
    # создание файла с настройками языка
    file = open('lists.py', 'x',)
    lst_key = ["vowl", "consonants", "noun", "adjective", "verb", "infinitive", "prefix", "suffix", "end", ]
    lst_value = []
    # запись настроек на файл
    for i in range(len(lst_key)):
        lst_value.append(list(input(f"Введите через запятую {lst_key[i]}\n").split(', ')))
    file.write(f'lang_settings={dict(zip(lst_key,lst_value))}')
    file.close()
    print("Файл успешно создан")
    # исключение, в случае если файл уже есть на компе
except FileExistsError:
    print("Файл с настройками языка уже присутвстует на компьютере.\n\n"
          "Если хотите их изменить, удалите файл с помощью команды 'delete_settings'.\n"
          "Если вам лень, то вы можете внести изменения в ручную, открыв в виде блокнота файл 'lists.py'\n"
          "и внести новые значения после знака ':'.\n")

# подключаем созданный файл
import lists as stt

# переменные с настройками генерации
ln_wrd = 3
count = 1
pref = 1
suff = 1
end = 1
setting = (count,ln_wrd,pref,suff,end)

# создание переменных для генерации разных частей речи
word = Wg(stt.lang_settings['consonants'],stt.lang_settings['vowl'],stt.lang_settings['prefix'],
                stt.lang_settings['suffix'],stt.lang_settings['end'])
inf_word = Wg(stt.lang_settings['consonants'],stt.lang_settings['vowl'],stt.lang_settings['prefix'],
                stt.lang_settings['infinitive'])
noun_word = Wg(stt.lang_settings['consonants'], stt.lang_settings['vowl'], stt.lang_settings['prefix'],
                stt.lang_settings['noun'])
verb_word = Wg(stt.lang_settings['consonants'], stt.lang_settings['vowl'], stt.lang_settings['prefix'],
                stt.lang_settings['verb'])
adj_word = Wg(stt.lang_settings['consonants'], stt.lang_settings['vowl'], stt.lang_settings['prefix'],
                stt.lang_settings['adjective'])

print("Введите команду.\nДля выведения списка комманд пишите -h\n")

# обработка команд
while True:
    enter = input()
    if enter == '-h':
        print("Список команд\n"
              "gen -- для генерации слова по заданным настройкам\n"
              "settings -- отображение настроек языка\n"
              "get_stat_gen -- посмотреть настройки генерации слова\n"
              "set_stat_gen -- изменить настройки генерации слова\n"
              "inf -- для генерации слова в инфинитиве\n"
              "noun -- для генерации существительного\n"
              "verb -- для генерации глагола\n"
              "adject -- для генерации прилагательного\n"
              "delete_settings -- для удаления настроек языка\n")
    if enter == 'gen':
        word.gen(*setting)
    if enter == 'settings':
        get_settings()
    if enter == 'get_gen_settings':
        get_gen_settings()
    if enter == 'set_gen_settings':
        setting = set_gen_settings()
        print('Изменения приняты!\n',setting)
    if enter == 'inf':
        inf_word.gen(*setting)
    if enter == 'noun':
        noun_word.gen(*setting)
    if enter == 'verb':
        verb_word.gen(*setting)
    if enter == 'adject':
        adj_word.gen(*setting)
    if enter == 'delete_settings':
        del_settings()
