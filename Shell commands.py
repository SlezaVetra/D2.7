# Создать двух пользователей (с помощью метода User.objects.create_user)

>>> from news.models import *
>>> u1 = User.objects.create_user(username='Jesus')
>>> u2 = User.objects.create_user(username='Stalin')
>>> u3 = User.objects.create_user(username='Splinter')

<!-- Можно посмотреть пользователя выполнив команду: u1 (u и номер пользователя)

# Создать два объекта модели Author, связанные с пользователями

>>> Author.objects.create(authorUser=u1)
>>> Author.objects.create(authorUser=u2)
>>> Author.objects.create(authorUser=u3)

<!-- При удачном выполнении команды получим: <Author: Author object (1,2,3)>

# Добавить 4 категории в модель Category

>>> Category.objects.create(name='sport')
>>> Category.objects.create(name='politics')
>>> Category.objects.create(name='science')
>>> Category.objects.create(name='culture')

# Добавить 2 статьи и 1 новость

>>> author = Author.objects.get(id=1)

<!-- Проверить статью можно командой: author>

# Создаем посты:

>>> Post.objects.create(author=author, categoryType='NW', title='Марсоход исследует грунт Красной планеты', text='Марсоходу предстоит исследовать геологическое строение Марса, а также проводить химический анализ состава грунта и вести поиск биомолекул и биосигнатур.')
>>> Post.objects.create(author=author, categoryType='NW', title='Брейк-данс официально стал олимпийским видом спорта', text='Международный олимпийский комитет (МОК) официально добавил уличные танцы в стиле брейк-данс в медальный зачет на Олимпийских играх в Париже 2024 года.')
>>> Post.objects.create(author=author, categoryType='NW', title='«Мы – товарищи». Как курьеры продолжают Ozonборьбу', text='Забастовка курьеров компании затягивается. В воскресенье недовольные сотрудники ждали гендиректора, но тот так и не почтил их своим присутствием. В отместку они создали профсоюз и позвали в него коллег со всей России.')
>>> Post.objects.create(author=author, categoryType='NW', title=' Rage Against The Machine & Run the Jewels', text='The Rage Against The Machine tour will now start in the spring of 2022. Your tickets will be honored for the postponed shows. Refunds are available at the original point of purchase for 30 days if you are unable to… ')

<!-- Можно орбащаться к title: Post.objects.get(id=1).title
<!--                    title: Post.objects.get(id=2).title и так далее

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий)

>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=4))
>>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
>>> Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))

# Создать как минимум 4 комментария к 
# разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий)


>>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
>>> Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')
>>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='anytextbyauthor')
>>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=3).authorUser, text='anytextbyauthor')

# Применяя функции like() и dislike() к статьям/новостям и 
# комментариям, скорректировать рейтинги этих объектов

>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).dislike()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=2).dislike()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=2).dislike()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).dislike()

<!-- Можно посмотреть рейтинг командой: Comment.objects.get(id=4).rating

# Обновить рейтинги пользователей

>>> Author.objects.get(id=1).update_rating()
>>> Author.objects.get(id=2).update_rating()

>>> Author.objects.get(id=1)

>>> a = Author.objects.get(id=1)

>>> a.update_rating()

# Вывести username и рейтинг лучшего пользователя 
(применяя сортировку и возвращая поля первого объекта)

>>> a = Author.objects.order_by('-ratingAuthor')[:1]

<!-- Со срезом, чтобы получить первого автора

>>> a = Author.objects.order_by('-ratingAuthor')

<!-- Без среза

# Вывести дату добавления, username автора, рейтинг, заголовок 
и превью лучшей статьи, основываясь на лайках/дислайках к этой статье

>>> best_article = Post.objects.get(pk=Post.objects.all().order_by('-rating').values('id')[0]['id'])
>>> best_article

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье

>>> for i in Comment.objects.filter(post = Post.objects.all().order_by('-rating')[0]):
    i.show()







