import smtplib
from dotenv import dotenv_values
config = dotenv_values("pass.env")
send_name = 'evst1.6@yandex.ru'
recip_name = 'slam966@yandex.ru'
sub = 'Приглашение'
letter = """From: {send_name}\nTo: {recip_name}\n{sub}:\n\nПривет, %friend_name%! %my_name% приглашает тебя на сайт %website%!\n\n%website% — это новая версия онлайн-курса по программированию.\n\nИзучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.\n\nКак будет проходить ваше обучение на %website%? \n\n→ Попрактикуешься на реальных кейсах.\nЗадачи от тимлидов со стажем от 10 лет в программировании.\n→ Будешь учиться без стресса и бессонных ночей.\nЗадачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.\n→ Подготовишь крепкое резюме.\nВсе проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.\n\nРегистрируйся → %website%\nНа курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(send_name=send_name, recip_name=recip_name, sub=sub)
link = "%website%"
first_name = "%my_name%"
user_name = "%friend_name%"
letter = letter.replace(link, "https://dvmn.org/profession-ref-program/al.evst96/GPsR9/")
letter = letter.replace(first_name, "Александр")
letter = letter.replace(user_name, "Пользователь")
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(config['login'], config['password'])
server.sendmail(send_name, recip_name, letter)
server.quit()