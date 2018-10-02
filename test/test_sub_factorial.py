__author__ = "Sudheer"

from sub_factorial import sub_factorial


def test_sub_factorial():
    assert 0 == sub_factorial(1)
    assert 1 == sub_factorial(2)
    assert 9 == sub_factorial(4)
    assert 44 == sub_factorial(5)
    assert 265 == sub_factorial(6)
    assert 133496 == sub_factorial(9)
    assert 32071101049 == sub_factorial(14)
    assert (
        290131015521620609254546237518688936375622413566095185632876940298382875066633305125595907908697818551860745708196640009079772455670451355426573609799907339222509103785567575227183775791345718826220455840965346196540544976439608810006794385963854831693077054723298130736781093200499800934036993104223443563872463385599425635345341317933466521378117877578807421014599223577201
        == sub_factorial(200)
    )
