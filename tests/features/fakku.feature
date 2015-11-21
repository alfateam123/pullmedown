Feature: download from fakku.net
    In order to read doujins from fakku.net
    As serial fappers
    I want to automatically download them

    Scenario: Non-existant manga
       Given I want to download https://www.fakku.net/manga/asfsdjljew342435fvds
       When I download it
       Then pullmedown says it cannot find it

    Scenario: Nice manga
       Given I want to download https://www.fakku.net/manga/high-girl-english
       When I download it
       Then 5 images have been downloaded

    Scenario: Nice doujin
       #Given I want to download https://www.fakku.net/doujinshi/the-commanders-submission-english
       Given I want to download https://www.fakku.net/doujinshi/you-actually-want-to-do-it-right-english 
       When I download it
       Then 39 images have been downloaded

    Scenario: Fakku Book
       Given I want to download https://www.fakku.net/manga/curiosity-xxxed-the-cat-english
       When I download it
       Then pullmedown says it's a book

    Scenario: Fakku Subscription
       Given I want to download https://www.fakku.net/manga/tale-of-a-couple-5-seconds-after-confession-english
       When I download it
       Then pullmedown says you have to subscribe
