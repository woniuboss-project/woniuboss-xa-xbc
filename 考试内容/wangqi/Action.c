Action()
{
	//检查点
	web_reg_find("SaveCount=home_chenk",
		"Text=专属宠物店的营销小助手",
		LAST);

	//打开首页
	web_url("web_url",
		"URL=https://snailpet.com/index",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
    //打印
	lr_log_message(lr_eval_string("{home_check}"));
    
    
    //检查点
	web_reg_find("SaveCount=login_data",
		"Text=打开钱箱",
		LAST);

	
	//登录
	web_submit_data("login_data",
		"Action=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=password", "Value=wangqi123456", ENDITEM,
		"Name=phone", "Value=18709143371", ENDITEM,
		"Name=shop_id", "Value=null", ENDITEM,
		LAST);
	//打印
	lr_log_message(lr_eval_string("{login_data}"));

	//判断
	if(atoi(lr_eval_string("{login_data}"))==1){
	        

	        lr_log_message("test login-pass");

	}else{
		lr_log_message("test login-fail");
	
	}

	//检查销售出库
	web_reg_save_param_regexp(
		"ParamName=conf_resp",
		"RegExp=[0-9]+",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	//发送post
	web_submit_data("market_data",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_page", "Value=首页", ENDITEM,
		"Name=ex_kind", "Value=点击", ENDITEM,
		"Name=ex_next_page", "Value=查询销售", ENDITEM,
		"Name=ex_title", "Value=查询销售", ENDITEM,
		"Name=shop_id", "Value=17553", ENDITEM,
		LAST);

	lr_log_message(lr_eval_string("{market_data}"));
	
	//判断
	if(atoi(lr_eval_string("{market_data}"))>0){
	        
	        lr_log_message("test market-pass");

	}else{
		lr_log_message("test market-fail");	
	}
	
	//检查点
	web_reg_save_param_regexp(
		"ParamName=expend_resp",
		"RegExp=[0-9]+",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	//发送支出post

	web_submit_data("expend_data",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_page", "Value=首页", ENDITEM,
		"Name=ex_kind", "Value=点击", ENDITEM,
		"Name=ex_next_page", "Value=支出", ENDITEM,
		"Name=ex_title", "Value=支出", ENDITEM,
		"Name=shop_id", "Value=17553", ENDITEM,
		LAST);

	lr_log_message(lr_eval_string("{expend_data}"));
	
	//判断
	if(atoi(lr_eval_string("{expend_data}"))>0){
	        
	        lr_log_message("test expend-pass");

	}else{
		lr_log_message("test expend-fail");	
	}

	//检查点
	web_reg_save_param_regexp(
		"ParamName=steat_resp",
		"RegExp=[0-9]+",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//发送报表post
	web_submit_data("steat_data",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_page", "Value=首页", ENDITEM,
		"Name=ex_kind", "Value=点击", ENDITEM,
		"Name=ex_next_page", "Value=报表", ENDITEM,
		"Name=ex_title", "Value=报表", ENDITEM,
		"Name=shop_id", "Value=17533", ENDITEM,
		LAST);

	
	lr_log_message(lr_eval_string("{steat_data}"));
	
	//判断
	if(atoi(lr_eval_string("{steat_data}"))>0){
	        
	        lr_log_message("test steat-pass");

	}else{
		lr_log_message("test steat-fail");	
	}

	
	return 0;
}
