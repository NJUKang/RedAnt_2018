var showAlert=function(){
	$("#model-alertInfo").css("display","block");
	$("#model-alertInfo .model-container").animate({opacity:"1",top:"30%"},300);
}
var closeAlert=function(){
	$("#model-alertInfo").css("display","none");
	$("#model-alertInfo .model-container").css("opacity","0.2");
	$("#model-alertInfo .model-container").css("top","29%");
}


function alertInfoWithJump(msg,url){
	// $("#model").css("display","none");
	showAlert();
	$("#model-alertInfo .model-body .message")[0].innerHTML=msg;
	$("#model-alertInfo .model-end .get").click(function(){
		location.href=url;
	})
	$("#model-alertInfo .model-container .fa-close").click(function(){
		location.href=url;
	});
}
function alertInformation(msg){
	// $("#model").css("display","none");
	showAlert();
	$("#model-alertInfo .model-body .message")[0].innerHTML=msg;
	$("#model-alertInfo .model-end .get").click(function(){closeAlert()});
	$("#model-alertInfo .model-container .fa-close").click(function(){closeAlert()});
}

// $("#model-alertInfo .model-end .shut").click(function(){
// 		$("#model-alertInfo").css("display","none");
// })