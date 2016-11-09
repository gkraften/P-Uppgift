class Highscore:
    _highscore = None
    _has_loaded = False

    @classmethod
    def load(cls, path):
        '''Loads highscore from path. If en exception occurs, the highscore
        is set to zero and False is returned. If it is loaded correctly True
        is returned. If the highscore has already been loaded it will be
        overwritten in memory.'''

        try:
            with open(path, "r") as file
                cls._highscore = int(file.readline())

            cls._has_loaded = True

            return True
        except:
            cls._highscore = 0
            cls._has_loaded = True

            return False

    @classmethod
    def has_loaded(cls):
      '''Returns whether the highscore has already been loaded.'''

      return cls._has_loaded

    @classmethod
    def get_highscore(cls):
      '''Returns the highscore or None if it hasn't been loaded yet.'''

      return cls._highscore

    @classmethod
    def set_highscore(cls, score):
      '''Sets highscore. Does not check if it is higher than the loaded
      one.'''

      cls._highscore = score

    @classmethod
    def save(cls, path):
      '''Writes the highscore to path.'''

      with open(path, "w") as file:
        file.write(str(cls._highscore))