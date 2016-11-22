import os

assets_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + ".." + os.path.sep + "assets"

def get_asset(path):
    """Returns the path to an asset located in the assets
    foldder referenced to by path."""

    return assets_path + path.replace("/", os.path.sep)