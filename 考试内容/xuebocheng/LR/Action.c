Action()
{
	
 	lr_convert_string_encoding(lr_eval_string("{null}"),LR_ENC_UTF8 ,LR_ENC_SYSTEM_LOCALE,"null");
	//登录
	lr_start_transaction("login");

	web_reg_save_param_json(
		"ParamName=check_login",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body={\"password\":\"{password}\",\"phone\":\"{phone}\",\"shop_id\":null}",
		LAST);

	lr_output_message(lr_eval_string("{check_login}"));
	if(atoi(lr_eval_string("{check_login}"))==1){
		lr_end_transaction("login", LR_PASS);
	}else{
		lr_end_transaction("login", LR_FAIL);
	}
	
	
	//新增会员
	
	lr_start_transaction("ADD");

	web_reg_save_param_json(
		"ParamName=check_add",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	web_custom_request("add_customer",
		"URL=https://snailpet.com/v2/Members/add",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=",
		"Body={\"addr\": \"\",\"cardNumber\": \"\",\"mark\": \"\",\"name\": \"{name}\",\"pets\": \[{\"birthday\": \"\",\"mark\": \"\",\"name\": \"MM\",\"sex\": \"\",\"color\": \"\",\"weight_new\": 0,\"speciesId\": \"\"}],\"phone\": \"{phone}\",\"spare_phone\": \"\",\"sex\": \"\",\"is_spending_msg\": 1,\"is_open_upgrade\": 1,\"shopId\": \"17540\",\"member_tags\": "",\"shop_id\": 17540}",
	 	 LAST);
	lr_output_message(lr_eval_string("{check_add}"));
	
	if(atoi(lr_eval_string("{check_add}"))==1){
		lr_end_transaction("ADD", LR_PASS);
	}else{
		lr_end_transaction("ADD", LR_FAIL);
	}
	
	//新增商品
	lr_start_transaction("GOODS");

	web_reg_save_param_json(
		"ParamName=check_goods",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	
	web_custom_request("add_goods",
		"URL=https://snailpet.com/v2/Product/add",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body={\"shopId\":\"17540\",\"productId\":\"0\",\"isServer\":\"0\",\"name\":\"{gname}\",\"categoryId\":\"840396\",\"inPrice\":\"20\",\"outPrice\":\"50\",\"percentage\":\"0\",\"notice_stocks\":\"1\",\"weight\":\"0\",\"logo_images\":\"\",\"detail_images\":\"\",\"production_time\":\"\",\"brand_name\":\"\",\"version\":\"1\",\"shop_id\":\"17540\"}",
		LAST);
	
	lr_output_message(lr_eval_string("{check_goods}"));
	if(atoi(lr_eval_string("{check_goods}"))==1){
		lr_end_transaction("GOODS", LR_PASS);
	}else{
		lr_end_transaction("GOODS", LR_FAIL);
	}
	
	//新增支出
	lr_start_transaction("SHOP");

	web_reg_save_param_json(
		"ParamName=check_shop",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	web_custom_request("shop",
		"URL=https://snailpet.com/v2/Shop/addSpending",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=",
		"Body={\"actionTime\":\"1585324800\",\"type\":\"2\",\"mark\":\"\",\"amount\":\"{money}\",\"shopId\":\"17540\",\"shop_id\":\"17540\"}",
		LAST);
	
	lr_output_message(lr_eval_string("{check_shop}"));
	if(atoi(lr_eval_string("{check_shop}"))==1){
		lr_end_transaction("SHOP", LR_PASS);
	}else{
		lr_end_transaction("SHOP", LR_FAIL);
	}
	
	//新增盘点
	lr_start_transaction("PANDIAN");

	web_reg_save_param_json(
		"ParamName=check_pandian",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	web_custom_request("pandian",
		"URL=https://snailpet.com/v2/shop/stocktaking/save",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body={\"mark\":\"\",\"name\":\"{pandian}\",\"shop_id\":17540,\"user_id\":27357}",
		LAST);
	lr_output_message(lr_eval_string("{check_pandian}"));
	if(atoi(lr_eval_string("{check_pandian}"))==1){
		lr_end_transaction("PANDIAN", LR_PASS);
	}else{
		lr_end_transaction("PANDIAN", LR_FAIL);
	}
	
	return 0;

}
