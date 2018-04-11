
	var cm="",cp="";
	function isEmail(strEmail) {
	    if ((strEmail.search(/^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/) != -1)|| strEmail=='')
	        return true;
	    else
	        return false;
	}

	function checkMail(node) {
	    var tip = document.getElementById("check-mail");
	    var mail = node.value;
	    if( ! isEmail(mail) ){
	    	tip.style.opacity='1';
	    	tip.className='check fa fa-close';
	    	cm=false;
	    	return false;
	    }
	    else{
	    	cm=true;
	    	tip.className='check fa fa-check';
	    	tip.style.opacity='1';
	    }
	    if (mail=='') {
	    	tip.className='check fa';
	    	cm=true;
	    	tip.style.opacity='0';
	    }
	}
	function isPsw(strPsw) {
	    if (strPsw.search(/^[\\u4e00-\\u9fa5_a-zA-Z0-9-]{6,20}$/) != -1 || strPsw==""){
	        return true;
	    }
	    else{
	        return false;
	    }
	}

	function checkPsw(node) {
	    var tip = document.getElementById("check-psw");
	    var pwd = node.value;
	    if( ! isPsw(pwd) ){
	    	tip.style.opacity='1';
	    	tip.className='check fa fa-close';
	    	cp=false;
	    	return false;
	    }
	    else{
	    	cp=true;
	    	tip.className='check fa fa-check';
	    	tip.style.opacity='1';
	    }
	    if (pwd=='') {
	    	tip.className='check fa';
	    	cp=true;
	    	tip.style.opacity='0';
	    }
	}

	$("#login").click(function(e){
		e.preventDefault();
		if(cm==false||cp==false){
			return false;
		}
		var mail = $("#mail").val();
        var psw = $("#psw").val();
		$.ajax({
	        type:"POST",
	        url:"/index/sign_up/",
	        data:{
                "email": mail,
                "password": psw
	        },
	        success:function(data){
	        	if(data.code == 2) {
	        		$('.enter').load($("#login").attr('href'));
	        		location.href="/index/";
					alert(data.info);
					// $('#sign-up-container').load("sign-upJump.txt");
				}
				else{
                alert(data.info);
				}
	        },
            fail: function() {
            },
            error: function(response) {
            	// console.log(document.getElementById("login").href);//file://......./user-id.html
            	// console.log($("#login").attr('href'));//user-id.html
	        	$('.enter').load($("#login").attr('href'));
                alert("error");
            }
	    });
	});
