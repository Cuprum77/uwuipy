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
        Uwuipy(1, 1, 0, 0, 0).uwuify("https://example.com mailto:example@example.com", skip_urls=True)
        == "https://example.com mailto:example@example.com"
    )

def test_uwuify_segmented_simple():
    uwu = Uwuipy(1, 0.3, 0.3, 0.3, 1)
    text = "Hello @everyone! Check out https://example.com and http://test.io/page?arg=1 yeah! Also, say hi to <@123456789012345678> and <@!987654321098765432>, they’re in <#112233445566778899> with role <@&998877665544332211>."

    assert (
        Uwuipy(1, 1, 0, 0, 0).uwuify_segmented(
            "Hello world! https://example.com (this is in parenthesis)",
        )
        == [('Hello', 'H-Hewwo', False), 
            (' ', ' ', False), 
            ('world!', 'w-w-w-wowwd!', False), 
            (' ', ' ', False), 
            ('https://example.com', 'https://example.com', False), 
            (' ', ' ', False), 
            ('(this', '(this', False), 
            (' ', ' ', False), ('is', 'i-i-is', False), 
            (' ', ' ', False), ('in', 'i-i-in', False), 
            (' ', ' ', False), ('parenthesis)', 'p-pawenthesis)', False)
        ]
    )

def test_uwuify_segmented_simple_url():
    assert (
        Uwuipy(1, 0, 0, 0, 0).uwuify_segmented(
            "Check out https://example.com and http://test.io/page?arg=1", verify_urls=True
        )
        == [('Check', 'Check', False), 
            (' ', ' ', False), 
            ('out', 'out', False), 
            (' ', ' ', False), 
            ('https://example.com', 'https://example.com', True), 
            (' ', ' ', False), 
            ('and', 'awnd', False), 
            (' ', ' ', False), 
            ('http://test.io/page?arg=1', 'http://test.io/page?arg=1', True)]
    )


def test_uwuify_segmented_full():
    test_str = "Hey @everyone! Check out https://example.com and http://test.io/page?arg=1 yeah! Also, say hi to <@123456789012345678> and <@!987654321098765432>, they’re in <#112233445566778899> with role <@&998877665544332211>. Look at this emoji: :hello_this_is_a_bypass: and this real one <a:partyblob:123456789012345678>! Oh and don’t forget <@1234> and #random. Finally, here’s some normal text to uwuify owo rawr love ove nuzzle while testing URLs like ftp://files.server.net/data.zip and emojis like :smile: or <a:wave:987654321098765432> just to make sure everything works properly!"
    assert (
        Uwuipy(1, 0.3, 0.3, 0.3, 1).uwuify_segmented(
            test_str
        )
        == 
        [   ('Hey', 'H-Hey', False), 
            (' ', ' ', False), 
            ('', '(', False), 
            (None, ' ', False), 
            (None, '｡ᵘ', False), 
            (None, ' ', False), 
            (None, 'ᵕ', False), 
            (None, ' ', False), 
            (None, 'ᵘ', False), 
            (None, ' ', False), 
            (None, '｡)', False), 
            (None, ' ', False), 
            ('@everyone', '@ewewyownye', True), 
            ('!', '!!11', False), 
            (' ', ' ', False), 
            ('Check', 'Check', False), 
            (' ', ' ', False), 
            ('out', '***glomps', False), 
            (' ', ' ', False), 
            ('', 'and', False), 
            (None, ' ', False), 
            (None, 'huggles***', False), 
            (None, ' ', False), 
            (None, 'o-o-out', False), 
            (None, ' ', False), 
            ('https://example.com', 'https://example.com', False), 
            (' ', ' ', False), 
            ('and', 'a-awnd', False), 
            (' ', ' ', False), 
            ('', '***boops', False), 
            (None, ' ', False), 
            (None, 'your', False), 
            (None, ' ', False), 
            (None, 'nose***', False), 
            (None, ' ', False), 
            ('http://test.io/page?arg=1', 'http://test.io/page?arg=1', False), 
            (' ', ' ', False), 
            ('yeah!', 'y-yeah!!1!', False), 
            (' ', ' ', False), 
            ('Also,', '***pounces', False), 
            (' ', ' ', False), 
            ('say', 'on', False), 
            (' ', ' ', False), 
            ('hi', 'you***', False), 
            (' ', ' ', False), 
            ('to', 'Awso,', False), 
            (' ', ' ', False), 
            ('', 'say', False), 
            (None, ' ', False), 
            (None, 'hi', False), 
            (None, ' ', False), 
            (None, 'to', False), 
            (None, ' ', False), 
            ('<@123456789012345678>', '<@123456789012345678>', True), 
            (' ', ' ', False), 
            ('and', 'awnd', False), 
            (' ', ' ', False), 
            ('', '(◦ᵕ', False), 
            (None, ' ', False), 
            (None, '˘', False), 
            (None, ' ', False), 
            (None, 'ᵕ◦)', False), 
            (None, ' ', False), 
            ('<@!987654321098765432>', '<@!987654321098765432>', True), 
            (',', ',', False), 
            (' ', ' ', False), 
            ('they’re', 'they’we', False), 
            (' ', ' ', False), 
            ('in', '(⑅˘꒳˘)', False), 
            (' ', ' ', False), 
            ('', 'in', False), 
            (None, ' ', False), 
            ('<#112233445566778899>', '<#112233445566778899>', True), 
            (' ', ' ', False), 
            ('with', 'with', False), 
            (' ', ' ', False), 
            ('role', '***huggles', False), 
            (' ', ' ', False), 
            ('', 'tightly***', False), 
            (None, ' ', False), 
            (None, 'wowe', False), 
            (None, ' ', False), 
            ('<@&998877665544332211>', '<@&998877665544332211>', True), 
            ('.', '.', False), 
            (' ', ' ', False), 
            ('Look', 'Wook', False), 
            (' ', ' ', False), 
            ('at', '***walks', False), 
            (' ', ' ', False), 
            ('this', 'away***', False), 
            (' ', ' ', False), 
            ('emoji:', 'at', False), 
            (' ', ' ', False), 
            ('', 'this', False), 
            (None, ' ', False), 
            (None, 'emojyi:', False), 
            (None, ' ', False), 
            (None, '♥(。U', False), 
            (None, ' ', False), 
            (None, 'ω', False), 
            (None, ' ', False), 
            (None, 'U。)', False), 
            (None, ' ', False), 
            (':hello_this_is_a_bypass:', ':hewwo_this_is_a_bypass:', True), 
            (' ', ' ', False), 
            ('and', 'awnd', False), 
            (' ', ' ', False), 
            ('this', 'this', False), 
            (' ', ' ', False), 
            ('real', 'OwO', False), 
            (' ', ' ', False), 
            ('one', 'weaw', False), 
            (' ', ' ', False), 
            ('', 'ownye', False), 
            (None, ' ', False), 
            (None, '(ᵘʷᵘ)', False), 
            (None, ' ', False), 
            ('<a:partyblob:123456789012345678>', '<a:pawtybwob:123456789012345678>', True), 
            ('!', '!!1!', False), 
            (' ', ' ', False), 
            ('Oh', 'Owh', False), 
            (' ', ' ', False), 
            ('and', 'a-a-a-awnd', False), 
            (' ', ' ', False), 
            ('don’t', 'down’t', False), 
            (' ', ' ', False), 
            ('forget', 'fowget', False), 
            (' ', ' ', False), 
            ('<@1234>', '<@1234>', True), 
            (' ', ' ', False), 
            ('and', 'awnd', False), 
            (' ', ' ', False), 
            ('#random.', '#wawndom.', False), 
            (' ', ' ', False), 
            ('Finally,', 'Finyawwy,', False), 
            (' ', ' ', False), 
            ('here’s', '(˘ሠ˘)', False), 
            (' ', ' ', False), 
            ('some', 'h-h-h-hewe’s', False), 
            (' ', ' ', False), 
            ('normal', 'some', False), 
            (' ', ' ', False), 
            ('text', '(ᵕᴗ', False), 
            (' ', ' ', False), 
            ('to', 'ᵕ⁎)', False), 
            (' ', ' ', False), 
            ('uwuify', 'nyowmaw', False), 
            (' ', ' ', False), 
            ('owo', '***walks', False), 
            (' ', ' ', False), 
            ('rawr', 'away***', False), 
            (' ', ' ', False), 
            ('love', 'text', False), 
            (' ', ' ', False), 
            ('ove', '***cries***', False), 
            (' ', ' ', False), 
            ('nuzzle', 'to', False), 
            (' ', ' ', False), 
            ('while', 'u-u-u-uwuify', False), 
            (' ', ' ', False), 
            ('testing', ';;w;;', False), 
            (' ', ' ', False), 
            ('URLs', 'owo', False), 
            (' ', ' ', False), 
            ('like', '(◡', False), 
            (' ', ' ', False), 
            ('', '꒳', False), 
            (None, ' ', False), 
            (None, '◡)', False), 
            (None, ' ', False), 
            (None, '***runs', False), 
            (None, ' ', False), 
            (None, 'away***', False), 
            (None, ' ', False), 
            (None, 'waww', False), 
            (None, ' ', False), 
            (None, 'x3', False), 
            (None, ' ', False), 
            (None, '***runs', False), 
            (None, ' ', False), 
            (None, 'away***', False), 
            (None, ' ', False), 
            (None, 'wuv', False), 
            (None, ' ', False), 
            (None, '***boops', False), 
            (None, ' ', False), 
            (None, 'your', False), 
            (None, ' ', False), 
            (None, 'nose***', False), 
            (None, ' ', False), 
            (None, 'uv', False), 
            (None, ' ', False), 
            (None, '(◡', False), 
            (None, ' ', False), 
            (None, 'ሠ', False), 
            (None, ' ', False), 
            (None, '◡)', False), 
            (None, ' ', False), 
            (None, 'nyuzzwe', False), 
            (None, ' ', False), 
            (None, '^w^', False), 
            (None, ' ', False), 
            (None, '***glomps***', False), 
            (None, ' ', False), 
            (None, 'whiwe', False), 
            (None, ' ', False), 
            (None, 'testing', False), 
            (None, ' ', False), 
            (None, '(˘ε˘)', False), 
            (None, ' ', False), 
            (None, '***runs', False), 
            (None, ' ', False), 
            (None, 'away***', False), 
            (None, ' ', False), 
            (None, 'UWWs', False), 
            (None, ' ', False), 
            (None, 'wike', False), 
            (None, ' ', False), 
            ('ftp://files.server.net/data.zip', 'ftp://files.server.net/data.zip', False), 
            (' ', ' ', False), 
            ('and', 'awnd', False), 
            (' ', ' ', False), 
            ('emojis', 'e-e-e-emojyis', False), 
            (' ', ' ', False), 
            ('like', 'wike', False), 
            (' ', ' ', False), 
            ('', '(◡', False), 
            (None, ' ', False), 
            (None, 'ሠ', False), 
            (None, ' ', False), 
            (None, '◡)', False), 
            (None, ' ', False), 
            (None, '***screeches***', False), 
            (None, ' ', False), 
            (':smile:', ':smiwe:', True), 
            (' ', ' ', False), 
            ('or', 'ow', False), 
            (' ', ' ', False), 
            ('<a:wave:987654321098765432>', '<a:wawe:987654321098765432>', True), 
            (' ', ' ', False), 
            ('just', 'jyust', False), 
            (' ', ' ', False), 
            ('to', 'to', False), 
            (' ', ' ', False), 
            ('make', '(・\\`ω\\´・)', False), 
            (' ', ' ', False), 
            ('sure', 'make', False), 
            (' ', ' ', False), 
            ('everything', '***smirks', False), 
            (' ', ' ', False), 
            ('works', 'smugly***', False), 
            (' ', ' ', False), 
            ('properly!', 'suwe', False), 
            (None, ' ', False), 
            (None, 'ewewything', False), 
            (None, ' ', False), 
            (None, '***screeches***', False), 
            (None, ' ', False), 
            (None, 'wowks', False), 
            (None, ' ', False), 
            (None, '–', False), 
            (None, ' ', False), 
            (None, '̗̀', False), 
            (None, ' ', False), 
            (None, '(ᵕ꒳ᵕ)', False), 
            (None, ' ', False), 
            (None, '̖́-', False), 
            (None, ' ', False), 
            (None, 'pwopewwy!!1!', False)]
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
