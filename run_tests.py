import unittest

def run_all_tests():
    loader = unittest.TestLoader()

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(loader.discover('tests/_1completion'))
    result = runner.run(loader.discover('tests/_2generation'))
    result = runner.run(loader.discover('tests/_3refactoring'))
    result = runner.run(loader.discover('tests/_4debugging'))

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)

if __name__ == '__main__':
    run_all_tests()
