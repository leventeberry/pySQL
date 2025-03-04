import questionary

connectionConfig = questionary.Choice(
    "Configure Database Connection",
    1,
)

testConfig = questionary.Choice(
    "Test Database Connection",
    2,
)

exitApp = questionary.Choice(
    "Exit",
    "q",
)