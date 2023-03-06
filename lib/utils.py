import os

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

def check_inline_assets_in_copied_survey(surveysvc_sdk: object, user_id: int, survey_id: int) -> dict:
    """
    :func:`check_inline_assets_in_copied_survey` It checks whether the copied survey's page contains an inline assets
    after copying a survey or not
    :param surveysvc_sdk:   `object` SurveySvc SDK
    :param user_id:         `string/int` The ID of the user who owns the survey
    :param survey_id:      `string/int` The Survey ID
    :rtype: `dict`
    """
    try:
        survey_pages = fetch_all_pages_in_survey(surveysvc_sdk, user_id, survey_id)
        for page in survey_pages["output_log"]["$items"]:
            if page["heading"] == "page heading with in-line assets":
                if not len(page["inline_assets"]) > 0:
                    raise TryAgain("Waiting for verify inline assets in page heading")

    except Exception:
        allure.attach(pprint.pformat(survey_pages), name="response", attachment_type=allure.attachment_type.TEXT)
        raise
    return survey_pages