import os
import pprint

import allure
import yaml



def load_params(file_name, folder_name="student_api_input"):
    """
    :func:`load_params`: Load data from yaml file under `/data` folder.

    :param file_name: `string` name of the yaml file to be read.
    :param folder_name: (option) `string` name of folder under  /data/
        folder( as we have different folders for different svcs.)
    """
    # in ResponseAPI there are scenarios in which multiple files are passed
    # as input to the test script. In that case, this condition will be used.
    if isinstance(file_name, list):
        test_params = []
        for file_name in file_name:
            test_params.extend(
                yaml.load(
                    open(
                        os.path.join(
                            os.path.dirname(__file__), "..", "data/" + folder_name, file_name
                        )
                    ),
                    Loader=yaml.CLoader,
                )
            )
    else:
        test_params = yaml.load(
            open(os.path.join(os.path.dirname(__file__), "..", "data/" + folder_name, file_name)),
            Loader=yaml.CLoader,
        )

    return test_params