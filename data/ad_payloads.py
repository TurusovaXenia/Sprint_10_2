from enum import StrEnum

import pytest
from faker import Faker

from utils import helpers

fake = Faker("ru_RU")


class AdCategory(StrEnum):
    AUTO = "Авто"
    BOOKS = "Книги"
    GARDENING = "Садоводство"
    HOBBY = "Хобби"
    TECHNOLOGY = "Технологии"


class AdCondition(StrEnum):
    NEW = "Новый"
    USED = "Б/У"


class TestImages(StrEnum):
    FLOWER = "flower.jpeg"
    BEE = "bee.png"


def create_ad_payload(name=None,
                      category=AdCategory.AUTO,
                      condition=AdCondition.NEW,
                      price=None,
                      city=None,
                      description=None):
    return {
        "name": name or fake.catch_phrase(),
        "category": category,
        "condition": condition,
        "price": price or str(fake.random_int(min=100, max=560)),
        "city": city or fake.city(),
        "description": description or fake.text(max_nb_chars=20),
    }


def prepare_ad_with_image(payload: dict, image_name=TestImages.BEE):
    file_path = helpers.get_upload_file_path(image_name)
    return open(file_path, "rb")


def get_patch_payload():
    cases_data = [
        ("name", fake.catch_phrase()),
        ("price", str(fake.random_int(min=100, max=560))),
        ("category", AdCategory.HOBBY),
        ("condition", AdCondition.USED),
        ("description", fake.text(max_nb_chars=20)),
        ("city", fake.city())
    ]

    parametrized_cases = []

    for field, new_value in cases_data:
        full_payload = create_ad_payload()
        full_payload[field] = new_value
        case = pytest.param(field, full_payload, id=f"patch_{field}")
        parametrized_cases.append(case)

    return parametrized_cases
