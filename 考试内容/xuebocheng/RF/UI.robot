*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
login
    [Template]    login
    13709113328    123698745
    admin    123698745
    13709113328    admin

customer
    [Template]    add_customer
    小王    13322054414    COcO
    MING    \    123123
    miai    13200114455
    

shop
    [Template]    expend
    200    2020-03-27
    ABC    2020-03-27
    300    @#!

query_customer
    [Template]    query_customer
    小王
    mimi
    明月
    137022211445

edit_customer
    [Template]    edit_customer
    六六    13708855611    QQ
    18622114455    龙龙    --
    @    *    龙龙

*** Keywords ***
login
    [Arguments]    ${phone}    ${password}
    Open Browser    https://snailpet.com/index
    sleep    3
    Click Element    xpath=/html/body/div[3]/div/div/div[3]/div[2]
    Input Text    name=phone    ${phone}
    Input Password    name=password    ${password}
    Click Element    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    Wait Until Element Is Visible    link=安全退出
    Element Should Contain    link=安全退出    安全退出
    [Teardown]    Close Browser

add_customer
    [Arguments]    ${name}    ${phone}    ${petName}
    Open Browser    https://snailpet.com/index
    sleep    3
    Click Element    xpath=/html/body/div[3]/div/div/div[3]/div[2]
    Input Text    name=phone    13709113328
    Input Password    name=password    123698745
    Click Element    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    Wait Until Element Is Visible    link=安全退出
    Click Element    xpath=/html/body/app-root/div/snail-menu-nav/div/a[2]/div[1]
    Sleep    10
    Wait Until Element Is Visible    link=新增会员
    Click Element    css=html body app-root div.main snail-member-main snail-members div.wn-body div.content div.screen-box.clearfix.menu-member-screen-box.up-types div.screen-edit-btn-new.clearfix a
    Input Text    name=name    ${name}
    Input Text    name=phone    ${phone}
    Input Text    name=petName    ${petName}
    Click Element    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[3]/div[2]
    sleep    10
    Element Should Contain    link=${name}    ${name}
    Log    success
    [Teardown]    Close Browser

expend
    [Arguments]    ${money}    ${data}
    [Timeout]
    Open Browser    https://snailpet.com/index
    sleep    3
    Click Element    xpath=/html/body/div[3]/div/div/div[3]/div[2]
    Input Text    name=phone    13709113328
    Input Password    name=password    123698745
    Click Element    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    Wait Until Element Is Visible    link=安全退出
    Click Element    link=支出
    sleep    5
    Click Element    xpath=/html/body/app-root/div/snail-else-main/snail-expend/div[1]/div[2]/div/a
    Click Element    xpath=/html/body/app-root/div/snail-else-main/snail-expend/div[2]/div/div/div[2]/div/div[2]/ul/li[14]
    Input Text    name=price    ${money}
    Input Text    name=date    ${data}
    Click Element    xpath=/html/body/app-root/div/snail-else-main/snail-expend/div[2]/div/div/div[3]/div[2]
    ${mone}    Get Text    xpath=/html/body/app-root/div/snail-else-main/snail-expend/div[1]/div[2]/div/div/span
    Run Keyword If    '${mone}'=='${money}元'    Log    success
    ...    ELSE    Log    FALSE
    [Teardown]    Close Browser

query_customer
    [Arguments]    ${searchInput}
    Open Browser    https://snailpet.com/index
    sleep    3
    Click Element    xpath=/html/body/div[3]/div/div/div[3]/div[2]
    Input Text    name=phone    13709113328
    Input Password    name=password    123698745
    Click Element    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    Wait Until Element Is Visible    link=安全退出
    Click Element    link=会员
    sleep    5
    Input Text    name=searchInput    ${searchInput}
    Click Element    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[1]/div/div[1]/div[9]/i
    ${name}    Get Text    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[1]/div/div[2]/table/tbody/tr/td[2]/a/span
    Run Keyword If    '${name}'!='${searchInput}'    Log    success
    ...    ELSE    Log    FALSE
    [Teardown]    Close Browser

edit_customer
    [Arguments]    ${name}    ${phone}    ${petName}
    Open Browser    https://snailpet.com/index
    sleep    3
    Click Element    xpath=/html/body/div[3]/div/div/div[3]/div[2]
    Input Text    name=phone    13709113328
    Input Password    name=password    123698745
    Click Element    xpath=/html/body/app-root/div/snail-index/div/div/div/div[3]/div/div[1]/a
    Wait Until Element Is Visible    link=安全退出
    Click Element    link=会员
    sleep    5
    Click Element    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[1]/div/div[2]/table/tbody/tr[1]/td[10]/a[3]
    Input Text    name=name    ${name}
    Input Text    name=phone    ${phone}
    Input Text    name=petName    ${petName}
    Click Element    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[2]/div/div/div[3]/div[2]
    ${names}    Get Text    xpath=/html/body/app-root/div/snail-member-main/snail-members/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/a/span
    Run Keyword If    '${names}'=='${name}'    Log    success
    ...    ELSE    Log    FALSE
    [Teardown]    Close Browser
