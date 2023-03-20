import argostranslate.package
import argostranslate.translate
import os

class Model:
  def __init__(self, device, from_code = 'en', to_code = 'ko'):
    self.from_code=from_code
    self.to_code=to_code
    os.environ["ARGOS_DEVICE_TYPE"]=device # auto, cpu, cuda
    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == self.from_code and x.to_code == self.to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

  def predict(self, text):
    return argostranslate.translate.translate(text, self.from_code, self.to_code)