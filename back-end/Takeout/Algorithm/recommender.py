import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs
import construct


def recommender():
    # 评分数据.
    ratings = tfds.load('movie_lens/100k-ratings', split="train")
    # 电影特征数据.
    movies = tfds.load('movie_lens/100k-movies', split="train")

    # 选取特征.
    ratings = ratings.map(lambda x: {
        "movie_id": tfds.strings.to_number(x["movie_id"]),
        "user_id": tfds.strings.to_number(x["user_id"])
    })
    movies = movies.map(lambda x: tfds.strings.to_number(x["movie_id"]))

    model = construct.Model()
    model.compile(optimizer=tfrs.keras.optimizers.Adagrad(0.5))

    # Randomly shuffle data and split between train and test.
    tf.random.set_seed(42)
    shuffled = ratings.shuffle(100_000, seed=42, reshuffle_each_iteration=False)

    train = shuffled.take(80_000)  # 取前8000做训练集
    test = shuffled.skip(80_000).take(20_000)  # 取80000-100000为测试集

    # Train.
    model.fit(train.batch(4096), epochs=5)

    # Evaluate.
    model.evaluate(test.batch(4096), return_dict=True)
