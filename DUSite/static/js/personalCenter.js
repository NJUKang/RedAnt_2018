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

var cp='',cf='',ca='',cpre='';
//验证密码
	function isPsw(strPsw) {
	    if (strPsw.search(/^[\\u4e00-\\u9fa5_a-zA-Z0-9-]{6,20}$/) != -1){
	    // if(strPsw.length!=0){
	        return true;
	    }
	    else{
	        return false;
	    }
	}

	function checkPsw(node) {
	    var tip = $("#psw").siblings(".check")[0];
	    var pwd = node.value;
	    if(pwd==""){
	    	tip.style.opacity='0';
	    	cp=false;
	    	if(conf!=""){
		    	confirmPsw(document.getElementById("cf-psw"));
		    }
	    	return false;
	    }
	    if( ! isPsw(pwd) ){
	    	tip.style.opacity='1';
	    	tip.className="fa fa-close check";
	    	tip.style.color="red";
	    	cp=false;
	    	return false;
	    }
	    else{
	    	cp=true;
	    	tip.style.opacity='1';
	    	tip.className="fa fa-check check";
	    	tip.style.color="green";
	    }
	    var conf=document.getElementById("cf-psw").value;
	    if(conf!=""){
	    	confirmPsw(document.getElementById("cf-psw"));
	    }
	    if(pwd==""){
	    	confirmPsw(document.getElementById("cf-psw"));
	    }
	}
	//确认密码
	function confirmPsw(node){
		var tip = document.getElementById("confirm-psw").getElementsByClassName("check")[0];
	    var pwd = node.value;
	    var proto=document.getElementById("psw").value;
	    if(pwd==""){
	    	tip.style.opacity='0';
	    	cf=false;
	    	return false;
	    }
	    if(proto==""&&pwd!=""){
	    	tip.style.opacity='0';
	    	cf=false;
	    	return false;
	    }
	    if( pwd == proto){
	    	tip.style.opacity='1';
	    	tip.className="fa fa-check check";
	    	tip.style.color="green";
	    	cf=true;
	    	if(proto==""){
	    		tip.style.opacity='0';
	    		cf=false;
	    	}
	    }
	    else{
	    	tip.style.opacity='1';
	    	tip.className="fa fa-close check";
	    	tip.style.color="red";
	    	cf=false;
	    	return false;
	    }
	}
function checkPrepsw(node){
	var initPsw="123456";//后端传未更改之前的密码
	var input=node.value;
	var tip = $("#prePsw").siblings(".check")[0];
	if(input==''){
		tip.style.opacity='0';
		cpre=false;
		return false;
	}
	if(initPsw!=input){
		tip.style.opacity='1';
    	tip.className="fa fa-close check";
    	tip.style.color="red";
		cpre=false;
		return false;
	}
	else{
		tip.style.opacity='1';
    	tip.className="fa fa-check check";
    	tip.style.color="green";
		cpre=true;
	}
}
var showHint=function(e){
	var id=e.name;
	var getHint="hint-"+id;
	var hintEl=document.getElementById(getHint);
	$(e).siblings("span.hint").css("opacity","1");
	if(id=="psw"){
		hintEl.innerHTML="可包含字母、数字、横线或下划线";
		$(hintEl).siblings("i").css("opacity","1");
	}
	else;
}
var hideHint=function(e){
	var id=e.name;
	var getHint="hint-"+id;
	var hintEl=document.getElementById(getHint);
	$(e).siblings("span.hint").css("opacity","0");
	$(hintEl).siblings("i").css("opacity","0");
}


// function setPsw(node){
// 	var Msg = document.getElementById("hint-psw");
// 	var tip = document.getElementById("psw-tip").getElementsByTagName('i');
// 	var pwd = node.value;
// 	    if(isPsw(pwd)){
// 	    	Msg.innerHTML ="可输入数字、字母、横线、下划线";
// 	    	tip[0].style.opacity='1';
// 	    }
// }
// function blurPsw(node){
// 	var Msg = document.getElementById("check-psw");
// 	var tip = document.getElementById("psw-tip").getElementsByTagName('i');
// 	var pwd = node.value;
// 	if(isPsw(pwd)){
// 	    	Msg.innerHTML ="";
// 	    	tip[0].style.opacity='0';
// 	    }
// }

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
		var num=form.getElementsByTagName('input').length;
		var errorMsg=new Array(num),tip=new Array(num),el=new Array(num);
		for(var i=0;i<num;i++){
			el[i]="#"+form.getElementsByTagName('input')[i].name;
			tip[i]=$(el[i]).siblings(".check")[0];
		}
		for(var i=0;i<num;i++){
			form.getElementsByTagName('input')[i].value='';
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
	var init;
	btn.on("click",function(){
		if ($(btn).hasClass("disable")) {
			$(input).css("border","1px solid #c8c8c8");
			$(input).css("background-color","hsla(0,0%,71%,.1)");
			$(input).css("padding","5px 10px");
			$(input).attr("disabled",false);
			this.innerHTML="取消";
			this.className="abled";
			init=$(input).val();
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

// var userImg;
// var Image=$(".change .change-userImag");
// console.log(Image);
// $(".change .change-userImag").on("change",function(){
// 	userImg=Image.get(0).files[0];
// 	console.log(userImg);
// 	if(userImg.length == 0){
// 	   alert('请选择文件');
// 	   return;
// 	}else{
// 	   var reader = new FileReader();//新建一个FileReader
// 	   reader.readAsText(userImg, "UTF-8");//读取文件 
// 	   reader.onload = function(evt){ //读取完文件之后会回来这里
// 	       var fileString = evt.target.result;
// 	       // form.file.value = fileString; //设置隐藏input的内容
// 	   		$(".change img").url=userImg.url;
// 	$.ajax({
// 		type:"POST",
//         url:"/setChanging",
//         cache:false,
//         data:{
//             "userImg": userImg
//         },
//         success:function(data){
// 			$(".change img").url=fileString;
//         },
//         fail: function() {
//             alert("failed");
//         },
//         error: function(response) {
//             alert("error");
//         }
// 	});}
// 	   }
// });





	$("#save").click(function(e){
		e.preventDefault();
		if($('#psw').value!=undefined)
			checkPsw($('#psw'));
		if($('#cf-psw').val()!=undefined)
			confirmPsw($('#cf-psw'));
		if ($("#prePsw").val()!=undefined)
			checkPrepsw($("#prePsw"));
		checkAccount($('#username'));
		// if(cp!=true||cf!=true || ca!=true||cpre!=true){
		// 	return false;
		// }
		var name = $("#username").val();
		var mail = $("#mail").val();
        var prePsw = $("#prePsw").val();
        var psw = $("#psw").val();
        var project =  jsonfy($("#pro-list li"));
		$.ajax({
	        type:"POST",
	        url:"/myaccount/",
	        // async:false,
	        cache:false,
	        data:{
                "username": name,
                "prePassword": prePsw,
                "password": psw,
                // "userImg": userImg,
                "email": mail,
                "project": project
	        },
	        success:function(data){
	        	if(data.code) {
	        		alertInfoWithJump(data.info,"/myaccount/");//修改成功改为保存成功，因为有时候没有修改
	        		// location.href=;
				}
				else {
                    alertInformation(data.info);
                }
	        },
            fail: function() {
                alertInformation("failed");
            },
            error: function(response) {
                alertInformation("error");
            }
	    });
	});


var jsonfy=function (el){
	var proList="{project list:";
	for(var i=0;i<$(el).length;i++){
		proList+="['";
		proList+=document.getElementById("pro-list").getElementsByTagName("li")[i].getElementsByTagName("span")[0].innerHTML;
		if(i==$(el).length-1)
			proList+="']";
		else
			proList+="'],";
	}
	proList+="}";
	console.log(proList);
	return proList;
}