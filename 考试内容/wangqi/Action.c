Action()
{
	//����
	web_reg_find("SaveCount=home_chenk",
		"Text=ר��������Ӫ��С����",
		LAST);

	//����ҳ
	web_url("web_url",
		"URL=https://snailpet.com/index",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
    //��ӡ
	lr_log_message(lr_eval_string("{home_check}"));
    
    
    //����
	web_reg_find("SaveCount=login_data",
		"Text=��Ǯ��",
		LAST);

	
	//��¼
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
	//��ӡ
	lr_log_message(lr_eval_string("{login_data}"));

	//�ж�
	if(atoi(lr_eval_string("{login_data}"))==1){
	        

	        lr_log_message("test login-pass");

	}else{
		lr_log_message("test login-fail");
	
	}

	//������۳���
	web_reg_save_param_regexp(
		"ParamName=conf_resp",
		"RegExp=[0-9]+",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	//����post
	web_submit_data("market_data",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_page", "Value=��ҳ", ENDITEM,
		"Name=ex_kind", "Value=���", ENDITEM,
		"Name=ex_next_page", "Value=��ѯ����", ENDITEM,
		"Name=ex_title", "Value=��ѯ����", ENDITEM,
		"Name=shop_id", "Value=17553", ENDITEM,
		LAST);

	lr_log_message(lr_eval_string("{market_data}"));
	
	//�ж�
	if(atoi(lr_eval_string("{market_data}"))>0){
	        
	        lr_log_message("test market-pass");

	}else{
		lr_log_message("test market-fail");	
	}
	
	//����
	web_reg_save_param_regexp(
		"ParamName=expend_resp",
		"RegExp=[0-9]+",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	//����֧��post

	web_submit_data("expend_data",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_page", "Value=��ҳ", ENDITEM,
		"Name=ex_kind", "Value=���", ENDITEM,
		"Name=ex_next_page", "Value=֧��", ENDITEM,
		"Name=ex_title", "Value=֧��", ENDITEM,
		"Name=shop_id", "Value=17553", ENDITEM,
		LAST);

	lr_log_message(lr_eval_string("{expend_data}"));
	
	//�ж�
	if(atoi(lr_eval_string("{expend_data}"))>0){
	        
	        lr_log_message("test expend-pass");

	}else{
		lr_log_message("test expend-fail");	
	}

	//����
	web_reg_save_param_regexp(
		"ParamName=steat_resp",
		"RegExp=[0-9]+",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	//���ͱ���post
	web_submit_data("steat_data",
		"Action=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=ex_current_page", "Value=��ҳ", ENDITEM,
		"Name=ex_kind", "Value=���", ENDITEM,
		"Name=ex_next_page", "Value=����", ENDITEM,
		"Name=ex_title", "Value=����", ENDITEM,
		"Name=shop_id", "Value=17533", ENDITEM,
		LAST);

	
	lr_log_message(lr_eval_string("{steat_data}"));
	
	//�ж�
	if(atoi(lr_eval_string("{steat_data}"))>0){
	        
	        lr_log_message("test steat-pass");

	}else{
		lr_log_message("test steat-fail");	
	}

	
	return 0;
}
