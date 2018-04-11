(function(){
	'use strict';
	var wrap=document.getElementById('u193');
	var button=document.getElementById('u190');
	var close=document.getElementById('u201');
	var send=document.getElementById('u200');
	var sendtip=document.getElementById('u205');
	button.addEventListener("click", show, false);
	close.addEventListener("click", clo, false);
	send.addEventListener("click", tip, false);
	function show(){
		if(wrap.classList.contains("contact-hidden")){
			wrap.classList.add("contact-visible");
			wrap.classList.remove("contact-hidden");
			wrap.style.visibility="visible";
			wrap.style.display="block";
		}
	}
	function clo(){
		wrap.classList.add("contact-hidden");
		wrap.classList.remove("contact-visible");
		wrap.style.visibility="hidden";
		wrap.style.display="none";
	}
	function tip(){
		clo();
		sendtip.style.visibility="visible";
		sendtip.style.display="block";
		setTimeout(function(){sendtip.style.display="none";sendtip.style.visibility="visible"},1200);
	}
})();