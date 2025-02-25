# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/distributed.ray.ipynb.

# %% auto 0
__all__ = ['RayBackend']

# %% ../nbs/distributed.ray.ipynb 4
from typing import Any

try:
    import ray
except ModuleNotFoundError as e:
    msg = (
        f'{e}. To use a ray cluster you have to install '
        'ray. Please run `pip install ray`. '
    )
    raise ModuleNotFoundError(msg) from e
from ..core import StatsForecast
from .core import ParallelBackend

# %% ../nbs/distributed.ray.ipynb 5
class RayBackend(ParallelBackend):
    def __init__(self, ray_address) -> None:
        self.ray_address = ray_address

    def forecast(self, df, models, freq, **kwargs: Any) -> Any:
        model = StatsForecast(df=df.set_index("unique_id"), models=models, freq=freq, ray_address=self.ray_address)
        return model.forecast(**kwargs)

    def cross_validation(self, df, models, freq, **kwargs: Any) -> Any:
        model = StatsForecast(df=df.set_index("unique_id"), models=models, freq=freq, ray_address=self.ray_address)
        return model.cross_validation(df, models, freq, **kwargs)
