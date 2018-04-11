// $(document).ready(function(){
// 	var change=document.getElementById('drop-menu').getElementsByTagName('i')[0];
// 	var ul=document.getElementById('personal-set');
// 	$("#drop-menu").mouseover(function(){
// 		$(ul).css("display","block");
// 		change.className="fa fa-angle-up";
// 	});
// 	$("#drop-menu").mouseout(function(){
// 		$(ul).css("display","none");
// 		change.className="fa fa-angle-down";
// 	});
// });

var cp='',cf='',ca='';
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
	    var tip = document.getElementById("psw-tip").getElementsByTagName('i');
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
	    var tip = document.getElementById("conf-tip").getElementsByTagName('i');
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
	    		errorMsg.innerHTML = "密码与上次输入不匹配";
	    	}
	    	else{
	    		tip[0].style.opacity='0';
	    		errorMsg.innerHTML = "";
	    	}
		    cf=false;
	    	return false;
	    }
	}
function setPsw(node){
	var Msg = document.getElementById("check-psw");
	var tip = document.getElementById("psw-tip").getElementsByTagName('i');
	var pwd = node.value;
	    if(isPsw(pwd)){
	    	Msg.innerHTML ="可输入数字、字母、横线、下划线";
	    	tip[0].style.opacity='1';
	    }
}
function blurPsw(node){
	var Msg = document.getElementById("check-psw");
	var tip = document.getElementById("psw-tip").getElementsByTagName('i');
	var pwd = node.value;
	if(isPsw(pwd)){
	    	Msg.innerHTML ="";
	    	tip[0].style.opacity='0';
	    }
}

var showBtn=document.getElementById('showSetPsw');
var hideBtn=document.getElementById('hideSetPsw');
var form=document.getElementsByClassName('change')[0].getElementsByClassName('set-psw')[0];
	showBtn.onclick=function(){
		$(form).css("display","block");
		$(showBtn).css("display","none");
	}
	hideBtn.onclick=function(){
		$(form).css("display","none");
		$(showBtn).css("display","block");
		var errorMsg=new Array(2),tip=new Array(2);
		errorMsg[0] = document.getElementById("check-psw");
	    tip[0] = document.getElementById("psw-tip").getElementsByTagName('i')[0];
	    errorMsg[1] = document.getElementById("check-cf-psw");
	    tip[1] = document.getElementById("conf-tip").getElementsByTagName('i')[0];
		var num=form.getElementsByTagName('input').length;
		for(var i=0;i<num;i++){
			form.getElementsByTagName('input')[i].value='';
			errorMsg[i].innerHTML='';
			tip[i].style.opacity='0';
		}
	}

	function checkAccount(node) {
	    var tip = document.getElementById("check-name");
	    var account = $.trim(node.value);
	    if (account.length < 2 && account.length>0) {
	        tip.getElementsByTagName("span")[0].innerHTML = " 用户名最少两位";
	        tip.style.opacity='1';
	        ca=false;
	        return false;
	    }
	    else if (account.length > 10) {
	        tip.getElementsByTagName("span")[0].innerHTML = " 用户名不能超过10位";
	        tip.style.opacity='1';
	        ca=false;
	        return false;
	    }
	    else {
	        tip.getElementsByTagName("span")[0].innerHTML = "";
	        tip.style.opacity='0';
	        ca=true;
	    }
	}


function removeList(){
	var proListEl=document.getElementsByClassName('pro-list')[0].getElementsByClassName('remove');
	for(var i=0;i<proListEl.length;i++){
		proListEl[i].addEventListener('click',function(){
			var par=this.parentNode;
			$(par).remove();
		})
	}
}
removeList();

function setUserName(){
	var btn=$("table tr.name a");
	var input=$("table tr.name input");
	var init=$(input).val();
	btn.on("click",function(){
		if ($(btn).hasClass("disable")) {
			$(input).css("border","1px solid #c8c8c8");
			$(input).css("background-color","hsla(0,0%,71%,.1)");
			$(input).css("padding","5px 10px");
			$(input).attr("disabled",false);
			this.innerHTML="取消";
			this.className="abled";
		}
		else{
				$(input).css("border","none");
				$(input).css("background-color","transparent");
				$(input).css("padding","5px 0");
				$(input).attr("disabled",true);
				this.innerHTML="修改用户名";
				this.className="disable";
				$(input).val(init);
				checkAccount(input);
		}
	});
}

setUserName();

var userImg;
var Image=$(".change .change-userImag");
console.log(Image);
$(".change .change-userImag").on("change",function(){
	userImg=Image.get(0).files[0];
	console.log(userImg);
	if(userImg.length == 0){
	   alert('请选择文件');
	   return;
	}else{
	   var reader = new FileReader();//新建一个FileReader
	   reader.readAsText(userImg, "UTF-8");//读取文件 
	   reader.onload = function(evt){ //读取完文件之后会回来这里
	       var fileString = evt.target.result;
	       // form.file.value = fileString; //设置隐藏input的内容
	   		$(".change img").url=userImg.url;
	$.ajax({
		type:"POST",
        url:"/setChanging",
        cache:false,
        data:{
            "userImg": userImg
        },
        success:function(data){
			$(".change img").url=fileString;
        },
        fail: function() {
            alert("failed");
        },
        error: function(response) {
            alert("error");
        }
	});}
	   }
});

	$("#save").click(function(e){
		e.preventDefault();
		if($('#psw').value!=undefined)
			checkPsw($('#psw'));
		if($('#cf-psw').val()!="")
			confirmPsw($('#cf-psw'));
		checkAccount($('#username'));
		// if(cp==false||cf==false || ca==false){
		// 	console.log("1");
		// 	return false;
		// }
		var name = $("#username").val();
		var mail = $("#mail").val();
        var psw = $("#psw").val();
        var project =  $("#pro-list").val();
		$.ajax({
	        type:"POST",
	        url:"/myaccount/",
	        // async:false,
	        cache:false,
	        data:{
                "username": name,
                "password": psw,
                "userImg": userImg,
                "email": mail,
                "project": project
	        },
	        success:function(data){
	        	if(data.code) {
	        		location.href="/myaccount/";
					alert(data.info);
					// $('#sign-up-container').load("sign-upJump.txt");
				}
				else {
                    alert(data.info);
                }
	        },
            fail: function() {
                alert("failed");
            },
            error: function(response) {
            	// console.log(document.getElementById("login").href);//file://......./user-id.html
            	// console.log($("#login").attr('href'));//user-id.html
                alert("error");
            }
	    });
	});