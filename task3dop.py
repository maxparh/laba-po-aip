from functools import reduce

news = {}
news['Курс биткоина вырос до 1000 долларов'] =  5
news['В новогоднюю ночь выйдет новая первая серия нового сезона "Шерлока"'] = 10
news['В Новосибирске из автобуса сбежала кондуктор'] = 7
news['Самолет «Почты России» вылетел с опозданием в несколько месяцев'] = 1
news['Козёл Тимур подружился с тигром Амуром'] = 20
news['Инженерам из Space X удалось посадить первую ступень ракеты на землю'] = 10

newsresult = {}
newsresult[1] = "Курс биткоина вырос до 1000 долларов"
newsresult[2] = "В новогоднюю ночь выйдет новая первая серия нового сезона Шерлока"
newsresult[3] = "В Новосибирске из автобуса сбежала кондуктор"
newsresult[4] = "Самолет «Почты России» вылетел с опозданием в несколько месяцев"
newsresult[5] = "Козёл Тимур подружился с тигром Амуром"
newsresult[6] = "Инженерам из Space X удалось посадить первую ступень ракеты на землю"

def chooseGoodNews(a, b, d):
    if a < b:
        print(d)
print(newsresult[1])
chooseGoodNews(news['Курс биткоина вырос до 1000 долларов'], news['В новогоднюю ночь выйдет новая первая серия нового сезона "Шерлока"'], newsresult[2])
chooseGoodNews(news['В новогоднюю ночь выйдет новая первая серия нового сезона "Шерлока"'], news['В Новосибирске из автобуса сбежала кондуктор'], newsresult[3])
chooseGoodNews(news['В Новосибирске из автобуса сбежала кондуктор'], news['Самолет «Почты России» вылетел с опозданием в несколько месяцев'], newsresult[4])
chooseGoodNews(news['Самолет «Почты России» вылетел с опозданием в несколько месяцев'], news['Козёл Тимур подружился с тигром Амуром'], newsresult[5])
chooseGoodNews(news['Козёл Тимур подружился с тигром Амуром'], news['Инженерам из Space X удалось посадить первую ступень ракеты на землю'], newsresult[6])