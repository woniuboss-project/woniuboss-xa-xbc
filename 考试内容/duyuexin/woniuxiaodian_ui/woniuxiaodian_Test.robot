*** Settings ***
Library           SeleniumLibrary
Resource          flow.txt

*** Test Cases ***
login
    登录流程    15332277492    dy940128

customer_add
    新增会员流程    张二    15869561268    小青

customer_delete
    删除会员流程

customer_modify
    修改会员流程    张蛋    18263561258    小芳

customer_query
    查询会员流程    狗少

storage_add
    新增商品流程    豆腐    5    20

storage_delete
    删除商品流程

storage_query
    查询商品流程    豆干

storage_ruku
    Flow.商品入库流程    20
