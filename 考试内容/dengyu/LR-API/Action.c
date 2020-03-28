Action()
{

	//定义登录检查点
	web_reg_save_param_json(
		"ParamName=login_result",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//发送登录的post请求
	web_custom_request("login_post",
		"URL=https://snailpet.com/v2/Passport/login",
		"Method=post",
		"TargetFrame=",
		"Resource=1",
		"Referer=",
		"Mode=HTTP",
		"RecContentType=application/json;charset=utf-8"
		"EncType=application/json;charset=utf-8",
		"Body={ \"phone\":\"{customerphone}\", \"password\":\"{customerpasswd}\",\"shop_id\":\"{status}\"}",
		LAST);
	
	 //登录断言
	if(atoi(lr_eval_string("{login_result}"))==0){
		lr_log_message("login test success");
	}else{
		lr_log_message("login test fail");
	}

	//新增会员检查点
	web_reg_save_param_json(
		"ParamName=add_result",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//新增会员请求
	web_custom_request("cus_add_post",
		"URL=https://snailpet.com/v2/Members/add",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"EncType=application/json",
		"Body={\"addr\":"", \"cardNumber\":"",\"mark \":"",\"name \": \"{name}\", \"pets\": [{\"birthday \": "",\"mark \": "",\"name \": \"{petname} \",\"sex \":"",\"color \": "" ,\"weight_new \": 0,\"speciesId \":""}],\"phone \":  \"{cphone} \",\"spare_phone\": "",\"sex \": 2,\"is_spending_msg \": 1,\"is_open_upgrade \": 1,\"shopId\":  \"17532 \",\"member_tags\": \"\",\"shop_id \": 17532}",
		LAST);
	

	//新增会员断言
	if(atoi(lr_eval_string("{add_result}"))==0){
		lr_log_message("customer add  test success");
	}else{
		lr_log_message("customer add  test fail");
	}
	
	//删除会员检查点
	web_reg_save_param_json(
		"ParamName=delete_result",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//删除会员请求
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Members/del",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"EncType=application/json",
		"Body={\"shopId\": \"17532\",\"memberId\": 586487,\"shop_id\": 17532}",
		LAST);

	
	//删除会员断言
	if(atoi(lr_eval_string("{delete_result}"))==0){
		lr_log_message("customer delete test success");
	}else{
		lr_log_message("customer delete test fail");
	}
	
	//会员卡管理检查点
	web_reg_save_param_json(
		"ParamName=card_add_result",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
		
	//会员卡管理请求
	web_custom_request("card_add_post",
		"URL=https://snailpet.com/v2/Shop/setMemberLevel",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTTP",
		"EncType=application/json",
		"Body={\"name\": \"hellow\",\"minPrice\": {amount},\"enablePlus\": 1,\"background\": 4,\"discount\": 10,\"discountForService\": 10,\"discount_for_combination\": 10,\"shopId\": 17532,\"shop_id\": 17532}",
		LAST);

	//会员卡管理断言
	if(atoi(lr_eval_string("{card_add_result}"))==0){
		lr_log_message("card add  test success");
	}else{
		lr_log_message("card add  test fail");
	}
	
	//门店支出检查点
	web_reg_save_param_json(
		"ParamName=cost_result",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//门店支出请求
	web_submit_data("web_submit_data",
		"Action=https://snailpet.com/v2/Shop/addSpending",
		"Method=POST",
		"EncType=application/x-www-form-urlencoded",
		"TargetFrame=",
		"Referer=",
		"Mode=HTTP",
		ITEMDATA,
		"Name=actionTim", "Value=${num}", ENDITEM,
		"Name=type", "Value=1", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=amount", "Value=${camount}", ENDITEM,
		"Name=shopid", "Value=17532", ENDITEM,
		"Name=shop_id", "Value=17532", ENDITEM,
		LAST);

	//门店支出断言
	if(atoi(lr_eval_string("{cost_result}"))==0){
		lr_log_message("cost test success");
	}else{
		lr_log_message("cost test fail");
	}
	
	return 0;
}
	
	
	
