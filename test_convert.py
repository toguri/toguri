from convert import to_celsius
def test_freezing():  # 0 °C になるはずが 32 °F → 0 °C に失敗する
    assert to_celsius(32) == 0
