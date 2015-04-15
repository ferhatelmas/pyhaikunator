__author__ = 'ferhat elmas'
__version__ = '0.0.4'

from random import choice, randint


class Haikunator:

    adjectives = """
        autumn hidden bitter misty silent empty dry dark summer
        icy delicate quiet white cool spring winter patient
        twilight dawn crimson wispy weathered blue billowing
        broken cold damp falling frosty green long late lingering
        bold little morning muddy old red rough still small
        sparkling throbbing shy wandering withered wild black
        young holy solitary fragrant aged snowy proud floral
        restless divine polished ancient purple lively nameless
    """.split()

    nouns = """
        waterfall river breeze moon rain wind sea morning
        snow lake sunset pine shadow leaf dawn glitter forest
        hill cloud meadow sun glade bird brook butterfly
        bush dew dust field fire flower firefly feather grass
        haze mountain night pond darkness snowflake silence
        sound sky shape surf thunder violet water wildflower
        wave water resonance sun wood dream cherry tree fog
        frost voice paper frog smoke star
    """.split()

    @classmethod
    def haikunate(cls, token_range=9999, delimiter='-'):
        if not isinstance(token_range, int) or token_range < 0:
            raise RuntimeError('Token range must be a nonnegative integer')
        if not isinstance(delimiter, str):
            raise RuntimeError('Delimiter must be a string')
        res = [choice(cls.adjectives), choice(cls.nouns)]
        r = randint(0, token_range)
        if r != 0:
            res.append(str(r))
        return delimiter.join(res)


if __name__ == '__main__':
    import re
    import unittest

    class Test(unittest.TestCase):

        def test_generate(self):
            self.assertTrue(re.match(r'\w+-\w+-\d+', Haikunator.haikunate()))

        def test_not_equal_in_repeated_calls(self):
            self.assertNotEqual(Haikunator.haikunate(), Haikunator.haikunate())

        def test_configurable_range(self):
            self.assertTrue(re.match(r'\w+-\w+-\d$', Haikunator.haikunate(9)))

        def test_drops_range_if_zero(self):
            self.assertTrue(re.match(r'\w+-\w+$', Haikunator.haikunate(0)))

        def test_configurable_delimiter(self):
            self.assertTrue(
                re.match(r'\w+~\w+~\d+', Haikunator.haikunate(delimiter='~'))
            )

        def test_drops_range_and_delimiter_if_zero(self):
            self.assertTrue(
                re.match(r'\w+ \w+$', Haikunator.haikunate(0, ' '))
            )

        def test_wrong_range(self):
            with self.assertRaises(RuntimeError):
                Haikunator.haikunate('1')
            with self.assertRaises(RuntimeError):
                Haikunator.haikunate(-1)

        def test_wrong_delimiter(self):
            with self.assertRaises(RuntimeError):
                Haikunator.haikunate(delimiter=1)

    unittest.main()
