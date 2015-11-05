Feature: download from fakku.net
    In order to read doujins from fakku.net
    As serial fappers
    I want to automatically download them

    Scenario: Non-existant manga
       Given I want to download https://www.fakku.net/manga/asfsdjljew342435fvds
       When I download it
       Then pullmedown says it cannot find it
