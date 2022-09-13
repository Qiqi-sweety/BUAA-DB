import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs


# Build a model.
class Model(tfrs.Model):

    def __init__(self):
        super().__init__()

        # user embedding.
        self.user_model = tfrs.keras.layers.Embedding(
            input_dim=2000, output_dim=64)
        # movie embedding.
        self.item_model = tfrs.keras.layers.Embedding(
            input_dim=2000, output_dim=64)

        # 在整个候选数据集上设置检索任务和评估指标。
        self.task = tfrs.tasks.Retrieval(
            metrics=tfrs.metrics.FactorizedTopK(
                candidates=movies.batch(128).map(self.item_model)
            )
        )

    def compute_loss(self, features: Dict[Text, tfrs.Tensor], training=False) -> tfrs.Tensor:
        user_embeddings = self.user_model(features["user_id"])
        movie_embeddings = self.item_model(features["movie_id"])

        return self.task(user_embeddings, movie_embeddings)
