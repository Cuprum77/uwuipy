import pytest
from uwuipy import Uwuipy


def test_uwuification_level_1():
    # Random assortment of Monty Python quotes.
    assert (
        Uwuipy(1, 0, 0, 0, 0, power=1).uwuify(
            "We want a shrubbery!! …Are you suggesting that coconuts migrate? "
            "Shut up! Will you shut up?! Ah, now we see the violence inherent in the system!"
        )
        == "We want a shwubbewy!! …Awe you suggesting that coconuts migwate? "
        "Shut up! Wiww you shut up?! Ah, now we see the viowence inhewent in the system!"
    )


def test_uwuification_level_2():
    # Monty Python reference combined with a Jojo reference (Kaz: I don't watch Jojo).
    assert (
        Uwuipy(1, 0, 0, 0, 0, power=2).uwuify("Jojo says no to the Knights of Ni!")
        == "Jyojyo says nyo to the Knyights of Nyi!"
    )


def test_uwuification_level_3():
    assert (
        Uwuipy(1, 0, 0, 0, 0, power=3).uwuify("Avali love to smell the roses!")
        == "Awawi wuv to smeww the woses!"
    )


def test_uwuification_level_4():
    assert (
        Uwuipy(1, 0, 0, 0, 0, power=4).uwuify(
            "Avali love to smell the roses! Oh! Don't put them on there! They'll melt! Don't give them an apple, either."
        )
        == "Awawi wuv to smeww the wowses! Owh! Down't put them own thewe! They'ww mewt! Down't giwe them awn appwe, eithew."
    )


def test_stuttering():
    assert (
        Uwuipy(1, 1, 0, 0, 0).uwuify("Hello world! (this is in parenthesis)")
        == "H-Hewwo w-w-w-wowwd! (this i-i-is i-i-in p-pawenthesis)"
    )


def test_url():
    assert (
        Uwuipy(1, 1, 0, 0, 0).uwuify("https://example.com mailto:example@example.com")
        == "https://example.com mailto:example@example.com"
    )


def test_guards():
    with pytest.raises(ValueError):
        Uwuipy(stutter_chance=-1)

    with pytest.raises(ValueError):
        Uwuipy(stutter_chance=2)

    with pytest.raises(ValueError):
        Uwuipy(power=0)

    with pytest.raises(ValueError):
        Uwuipy(power=5)
