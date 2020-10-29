function main(){
	let linkedin = document.getElementById('linkedin');
	let twitter = document.getElementById('twitter');
	let github = document.getElementById('github');
	// let form = document.getElementById('eform');
	linkedin.addEventListener("mouseover",linkedinHover);
	linkedin.addEventListener("mouseout",linkedinNorm);
	twitter.addEventListener("mouseover",twitterHover);
	twitter.addEventListener("mouseout",twitterNorm);
	github.addEventListener("mouseover", githubHover);
	github.addEventListener("mouseout", githubNorm);
	// form.addEventListener("submit",submitForm);
}

function linkedinHover(){
	linkedin.src="/static/media/linkedin_hover.png";
}

function twitterHover(){
	twitter.src="/static/media/twitter_hover.png";
}

function githubHover(){
	github.src="/static/media/github_hover.png"
}

function linkedinNorm(){
	linkedin.src="/static/media/linkedin.png";
}

function twitterNorm(){
	twitter.src="/static/media/twitter.png";
}

function githubNorm(){
	github.src="/static/media/github.png";
}

// function submitForm(){
// 	var formValid = false;
// 	var form = document.getElementById('eform');
// 	//var regEx = /\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\z/;
// 	var regEx = /(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])/;
//
// 	if (regEx.test(form.email.value)){
// 		formValid = true;
// 		document.getElementById("email").style.borderColor = "white";
// 		document.getElementById("name").style.borderColor = "white";
// 	}else{
// 		if (form.email.value == ""){
// 			document.getElementById("email").value = "Required";
// 		}
// 		document.getElementById("email").style.borderColor = "red";
// 		console.log(form.email.value + " is invalid.")
// 		event.preventDefault(event);
// 	}
// 	if (form.message.value == "" || form.message.value == "Required"){
// 		document.getElementById("message").style.borderColor = "red";
// 		document.getElementById("message").value = "Required"
// 		event.preventDefault(event);
// 	}else{
// 		formValid = true;
// 		document.getElementById("message").style.borderColor = "white";
// 		document.getElementById("name").style.borderColor = "white";
// 	}
// 	if (formValid){
// 		console.log("Submission valid.");
// 		alert("Unfortunately this feature is not fully developed.\nIf you wish to contact me, please do so through my email at: james@james-whale.com")
// 	}else{
// 		event.preventDefault(event);
// 		console.log("Submission invalid.")
// 	}
// }

var slideIndex = 1;

function forth(n){
	slideShow(slideIndex += n);
}

function currentSlide(n){
	slideShow(slideIndex = n);
}

function slideShow(n){
	var i;
	var slides = document.getElementsByClassName("slide");
	if (n > slides.length){slideIndex = 1}
	if (n < 1){slideIndex = slides.length}
	for (i = 0; i < slides.length; i++){
		slides[i].style.display = "none";
	}
	slideIndex++;
	if (slideIndex > slides.length){slideIndex = 1}
	slides[slideIndex-1].style.display = "block";
	setTimeout(slideShow, 10000);
}
