
if __name__ == '__main__':
    import utils.imageComparison
    from actionEnum import ActionWaitUntilType
    print(utils.imageComparison.is_template_appear_in_screenshot(ActionWaitUntilType.INSUFFICIENT_STAMINA_TEXT))