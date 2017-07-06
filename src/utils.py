"""User-available utilities."""
# ToDo: rename the module

from itertools import combinations

from src.lib import api_call
from src.models import WordSet


def get_common_terms(*api_envs):
    """Get all term duplicates across all user word sets."""
    response = api_call('sets', *api_envs)
    word_sets = []
    common_terms = []

    for word_set in response.json():
        word_sets.append(WordSet(word_set['title'], word_set['terms']))

    for word_set_1, word_set_2 in combinations(word_sets, 2):
        common_terms.append(
            (word_set_1, word_set_2, word_set_1.has_common(word_set_2)))
    return common_terms


def apply_regex(pattern, repl, set_name, *api_envs):
    """Apply regex replace to all terms in word set."""
    raise NotImplementedError  # ToDo: complete the utility
