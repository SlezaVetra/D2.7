
# Создать двух пользователей (с помощью метода User.objects.create_user)
User.objects.create_user('User1', 'User1@gmail.com', 'User1password')
User.objects.create_user('User2', 'User2@gmail.com', 'User2password')

# Создать два объекта модели Author, связанные с пользователями
Author.objects.create(user = User.objects.get(username = 'User1'))
Author.objects.create(user = User.objects.get(username = 'User2'))

# Добавить 4 категории в модель Category
Category.objects.create(category = 'sport')
Category.objects.create(category = 'politics')
Category.objects.create(category = 'science')
Category.objects.create(category = 'culture')

# Добавить 2 статьи и 1 новость
Post.objects.create(
    author = Author.objects.get(user = 1),
    post_type = 'article',
    title = 'Unknown Leonardo da Vinci',
    content = 'They called him “fat boy,” this seventeen-year old apprentice in the studio of Florentine painter Verrocchio who would receive care packages from his step-father, a pastry chef. The bastard son of a Florentine notary and a lady of Vinci, the boy’s doting step-father gave him a taste for marzipans and sugars from a very young age.',
)

Post.objects.create(
    author = Author.objects.get(user = 1),
    post_type = 'article',
    title = 'Bianca Sforza: Lady with a Secret',
    content = 'Bianca Sforza attracted few stares when introduced to the art world on January 30, 1998. She was just a pretty face in a frame to the crowd at a Christie\'s auction in New York City. Nobody knew her name at the time, or the name of the artist who had made the portrait. The catalog listed the work—a colored chalk-and-ink drawing on vellum—as early 19th century and German, with borrowed Renaissance styling. A New York dealer, Kate Ganz, purchased the picture for $21,850.',
)

Post.objects.create(
    author = Author.objects.get(user = 2),
    post_type = 'news',
    title = 'Supreme Court enters a new era of personal accusation and finger-pointing',
    content = 'Supreme Court justices have long criticized each other\'s legal reasoning, but they are increasingly impugning their colleagues\' motives and sincerity, in a way that matches the current political climate. The Roberts Court, with three appointees of former President Donald Trump now in place, appears to be entering a new era of personal accusation and finger-pointing.',
)

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий)
Post.objects.get(id = 1).category.add(Category.objects.get(category = "science"))
Post.objects.get(id = 1).category.add(Category.objects.get(category = "culture"))
Post.objects.get(id = 2).category.add(Category.objects.get(category = "culture"))
Post.objects.get(id = 3).category.add(Category.objects.get(category = "politics"))

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий)
Comment.objects.create(
    text = 'Nice one!',
    post = Post.objects.get(id = 1),
    author = User.objects.get(id = 1)
)

Comment.objects.create(
    text = 'I\'m impressed',
    post = Post.objects.get(id = 2),
    author = User.objects.get(id = 1)
)

Comment.objects.create(
    text = 'Already knew',
    post = Post.objects.get(id = 1),
    author =User.objects.get(id = 2)
)

Comment.objects.create(
    text = 'You can again and more slowly',
    post = Post.objects.get(id = 3),
    author = User.objects.get(id = 2)
)

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов
Post.objects.get(id = 1).like()
Post.objects.get(id = 1).like()
Post.objects.get(id = 1).like()
Post.objects.get(id = 2).like()
Post.objects.get(id = 2).dislike()
Post.objects.get(id = 2).like()
Post.objects.get(id = 2).like()
Post.objects.get(id = 3).dislike()
Post.objects.get(id = 3).dislike()
Post.objects.get(id = 3).dislike()

Comment.objects.get(id = 1).like()
Comment.objects.get(id = 1).like()
Comment.objects.get(id = 2).like()
Comment.objects.get(id = 2).dislike()
Comment.objects.get(id = 2).like()
Comment.objects.get(id = 3).dislike()
Comment.objects.get(id = 3).dislike()
Comment.objects.get(id = 3).like()
Comment.objects.get(id = 4).dislike()
Comment.objects.get(id = 4).dislike()
Comment.objects.get(id = 4).dislike()

# Обновить рейтинги пользователей
Author.objects.get(id = 1).update_rating()
Author.objects.get(id = 2).update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта)
Author.objects.all().order_by('-rating').values('user__username', 'rating')[0]

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье
Post.objects.all().order_by('-rating').values('create_data', 'author__user__username', 'rating', 'title')[0]
Post.objects.all().order_by('-rating')[0].preview()

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье
for i in Comment.objects.filter(post = Post.objects.all().order_by('-rating')[0]):
    i.show()
