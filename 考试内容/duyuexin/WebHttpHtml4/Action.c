Action()
{
	
	
	web_reg_save_param_json(
		"ParamName=resp",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

    //定义一个登录请求
	web_submit_data("web_submit_data",
		"Action=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=password", "Value=dy940128", ENDITEM,
		"Name=phone", "Value=15332277492", ENDITEM,
		"Name=shop_id", "Value=null", ENDITEM,
		LAST);
    
	if(atoi(lr_eval_string("{resp}")) == 0){
		lr_output_message("login test pass");
	}else{
		lr_output_message("login test fail");
	}

    
	web_reg_save_param_json(
		"ParamName=del_resp",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//会员删除请求
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Members/del",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"shopId\": \"17549\",\"memberId\": 586252,\"shop_id\": 17549}",
		LAST);
	
	if(atoi(lr_eval_string("{resp}")) == 0){
		lr_output_message("del customer test pass");
	}else{
		lr_output_message("del customer test pass");
	}

	web_reg_save_param_json(
		"ParamName=add_resp",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//新增会员请求
	web_submit_data("add_customer_data",
		"Action=https://snailpet.com/v2/Members/add",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=addr", "Value=", ENDITEM,
		"Name=cardNumber", "Value=", ENDITEM,
		"Name=is_open_upgrade", "Value=1", ENDITEM,
		"Name=is_spending_msg", "Value=1", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=member_tags", "Value=", ENDITEM,
		"Name=name", "Value=特兰股", ENDITEM,
		"Name=pets", "Value=[0].name=大单", ENDITEM,
		"Name=phone", "Value=15935656958", ENDITEM,
		"Name=sex", "Value=", ENDITEM,
		"Name=shop_id", "Value=17546", ENDITEM,
		"Name=shopId", "Value=17546", ENDITEM,
		"Name=spare_phone", "Value=", ENDITEM,
		LAST);
	if(atoi(lr_eval_string("{add_resp}")) == 0){
		lr_output_message("add customer test pass");
	}else{
		lr_output_message("add customer test pass");
	}
	
	
	web_reg_save_param_json(
		"ParamName=del_goods_resp",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//删除商品请求
	web_submit_data("web_submit_data",
		"Action=https://snailpet.com/v2/Product/delByIds",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=shopld", "Value=17549", ENDITEM,
		"Name=product_ids", "Value=2134198", ENDITEM,
		"Name=shop_id", "Value=17549", ENDITEM,
		LAST);
	if(atoi(lr_eval_string("{del_goods_resp}")) == 0){
		lr_output_message("del goods test pass");
	}else{
		lr_output_message("del goods test pass");
	}
	
	web_reg_save_param_json(
		"ParamName=storage_resp",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//商品入库请求
	web_submit_data("web_submit_data",
		"Action=https://snailpet.com/v2/product/update/stocks",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=exp_time", "Value=null", ENDITEM,
		"Name=inPrice", "Value=5", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=number", "Value=20", ENDITEM,
		"Name=productld", "Value=2134162", ENDITEM,
		"Name=production_time", "Value=null", ENDITEM,
		"Name=shelf_life", "Value=0", ENDITEM,
		"Name=shop_id", "Value=17549", ENDITEM,
		"Name=shopld", "Value=17549", ENDITEM,
		LAST);
	if(atoi(lr_eval_string("{storage_resp}")) == 0){
		lr_output_message("stor goods test pass");
	}else{
		lr_output_message("stor goods test pass");
	}
	return 0;
}
