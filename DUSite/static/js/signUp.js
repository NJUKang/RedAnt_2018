'use strict';

	var cm='',cp='',ca='',cf='';
	//验证邮箱
	function isEmail(strEmail) {
	    if ((strEmail.search(/^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/) != -1)|| strEmail=='')
	        return true;
	    else
	        return false;
	}

	function checkMail(node) {
	    var errorMsg = document.getElementById("check-mail");
	    var tip = document.getElementById("sign-up-mail").getElementsByTagName('i');
	    var mail = node.value;
	    errorMsg.innerHTML = isEmail(mail) ? "" : "邮箱格式不正确";
	    if( ! isEmail(mail) ){
	    	tip[0].style.opacity='1';
	    	cm=false;
	    	return false;
	    }
	    else{
	    	cm=true;
	    	tip[0].style.opacity='0';
	    }
	}

	//验证密码
	function isPsw(strPsw) {
	    if (strPsw.search(/^[\\u4e00-\\u9fa5_a-zA-Z0-9-]{6,20}$/) != -1 || strPsw==""){
	    // if(strPsw.length!=0){
	        return true;
	    }
	    else{
	        return false;
	    }
	}

	function checkPsw(node) {
	    var errorMsg = document.getElementById("check-psw");
	    var tip = document.getElementById("sign-up-psw").getElementsByTagName('i');
	    var pwd = node.value;
	    if( ! isPsw(pwd) ){
	    	tip[0].style.opacity='1';
	    	errorMsg.innerHTML = "密码格式不正确";
	    	cp=false;
	    	return false;
	    }
	    else{
	    	cp=true;
	    	errorMsg.innerHTML ="";
	    	tip[0].style.opacity='0';
	    }
	    var conf=document.getElementById("cf-psw").value;
	    if(conf!=""){
	    	confirmPsw(document.getElementById("cf-psw"));
	    }
	}
	//确认密码
	function confirmPsw(node){
		var errorMsg = document.getElementById("check-cf-psw");
	    var tip = document.getElementById("confirm-psw").getElementsByTagName('i');
	    var pwd = node.value;
	    var proto=document.getElementById("psw").value;
	    // if(proto==""){
	    // 	checkPsw(document.getElementById("psw"));
	    // 	tip[0].style.opacity='1';
	    // 	cf=false;
	    // 	errorMsg.innerHTML = "请在上栏中输入密码";
	    // }
	    if( pwd == proto || pwd==""){
	    	errorMsg.innerHTML="";
	    	cf=true;
	    	tip[0].style.opacity='0';
	    }
	    else{
	    	if(proto!=""){
		    	tip[0].style.opacity='1';
		    	cf=false;
	    		errorMsg.innerHTML = "密码与上次输入不匹配";
	    	}
	    	else{
	    		tip[0].style.opacity='0';
		    	cf=false;
	    		errorMsg.innerHTML = "";
	    	}
	    	return false;
	    }
	}

	//验证账号
	function checkAccount(node) {
	    var errorMsg = document.getElementById("check-name");
	    var tip = document.getElementById("sign-up-name").getElementsByTagName('i');
	    var account = $.trim(node.value);
	    if (account.length < 2 && account.length>0) {
	        errorMsg.innerHTML = "用户名最少两位";
	        tip[0].style.opacity='1';
	        ca=false;
	        return false;
	    }
	    else if (account.length > 10) {
	        errorMsg.innerHTML = "用户名不能超过10位";
	        tip[0].style.opacity='1';
	        ca=false;
	        return false;
	    }
	    else {
	        errorMsg.innerHTML = "";
	        tip[0].style.opacity='0';
	        ca=true;
	    }
	}


	$("#sign-up").on("submit",function(e){
		e.preventDefault();
		if(cm!=true || ca!=true || cp!=true ||cf!=true){
			alert("请完善表单");
			return false;
		}
		var name = $("#name").val();
		var mail = $("#mail").val();
        var psw = $("#psw").val();
		$.ajax({
	        type:"POST",
	        url:"/index/sign_up/",
	        async:false,
	        cache:false,
	        data:{
	            "username": name,
                "email": mail,
                "password": psw
	        },
	        success:function(data){
	        	if(data.code) {
	        		$('#sign-up-container').load("sign-upJump.txt");
					location.href="/index/";
					alert(data.info);
					// $('#sign-up-container').load("sign-upJump.txt");
				}
				else {
                    alert(data.info);
                }
	        },
            fail: function() {
				e.preventDefault();
                alert("failed");
            },
            error: function(response) {
				e.preventDefault();
                alert("error");
                // $("html").load("test.php");
            }
	    });
	});



	//表单总校验
	// function check(){
	// 	if(cm==false || ca==false || cp==false ||cf==false){
	// 		e.preventDefault();
	// 		return false;
	// 	}
	// 	console.log("111");
	//     $.ajax({
	//         type:"POST",
	//         url:"test.php",
	//         async:true,
	//         cache:false,
	//         data:{
	//             "username": $('#name').value,
 //                "email": $('#mail').value,
 //                "password": $('#psw').value
	//         },
	//         success:function(data){
	//         	alert("注册成功");
	//             $('#sign-up-container').load("sign-upJump.txt");
	//         },
 //            fail: function() {
 //                alert("failed");
 //            },
 //            error: function(response) {
 //                alert("error");
 //                // $("html").load("test.php");
 //            }
	//     });
	// }